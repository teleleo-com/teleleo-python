#!/usr/bin/env python3
"""Generate the models, resources, API reference and operation tests of the SDK from spec/openapi.yaml.

    python scripts/generate.py

Hand-written code lives in src/teleleo/_*.py; everything this script writes starts with a "generated" header.
"""

from __future__ import annotations

import keyword
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pydantic
import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "openapi.yaml"
PKG = ROOT / "src" / "teleleo"
HEADER = "# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.\n"

# Client attribute -> (class name stem, spec tag for the docstring)
RESOURCES: Dict[str, Tuple[str, str]] = {
    "dongles": ("Dongles", "Dongle"),
    "sms": ("Sms", "Sms"),
    "calls": ("Calls", "Call"),
    "ussd": ("Ussd", "Ussd"),
    "contacts": ("Contacts", "Contact"),
    "contact_groups": ("ContactGroups", "ContactGroup"),
    "mailings": ("Mailings", "Mailing"),
    "redirections": ("Redirections", "Redirection"),
    "call_scenarios": ("CallScenarios", "CallScenario"),
    "follow_up_sms_settings": ("FollowUpSmsSettings", "FollowUpSms"),
    "public_vpn": ("PublicVpn", "PublicVpn"),
    "socks_proxies": ("SocksProxies", "DongleSocksProxy"),
    "sip_users": ("SipUsers", "Sip"),
    "files": ("Files", "File"),
}

# operationId -> (client attribute, method name). Every operation of the spec must be listed.
OPERATIONS: Dict[str, Tuple[str, str]] = {
    "listDongles": ("dongles", "list"),
    "getDongle": ("dongles", "get"),
    "updateDongle": ("dongles", "update"),
    "rebootDongle": ("dongles", "reboot"),
    "enableDongleWifi": ("dongles", "enable_wifi"),
    "disableDongleWifi": ("dongles", "disable_wifi"),
    "setDongleWifiCredentials": ("dongles", "set_wifi_credentials"),
    "enableDongleWifiExtender": ("dongles", "enable_wifi_extender"),
    "disableDongleWifiExtender": ("dongles", "disable_wifi_extender"),
    "scanDongleWifiNetworks": ("dongles", "scan_wifi_networks"),
    "updateDongleOfflineNotification": ("dongles", "update_offline_notification"),
    "setDongleNumber": ("dongles", "set_number"),
    "getDongleNetworkInfo": ("dongles", "get_network_info"),
    "getDongleSimIdentifiers": ("dongles", "get_sim_identifiers"),
    "listDongleStatistics": ("dongles", "list_statistics"),
    "listSms": ("sms", "list"),
    "listDongleSms": ("sms", "list_for_dongle"),
    "getSms": ("sms", "get"),
    "updateSms": ("sms", "update"),
    "deleteSms": ("sms", "delete"),
    "sendSms": ("sms", "send"),
    "sendSmsToContact": ("sms", "send_to_contact"),
    "replyToSms": ("sms", "reply"),
    "listSmsThreads": ("sms", "list_threads"),
    "listCalls": ("calls", "list"),
    "createCall": ("calls", "create"),
    "getCall": ("calls", "get"),
    "deleteCall": ("calls", "delete"),
    "listUssd": ("ussd", "list"),
    "sendUssd": ("ussd", "send"),
    "getUssd": ("ussd", "get"),
    "deleteUssd": ("ussd", "delete"),
    "deleteDongleUssds": ("ussd", "delete_all"),
    "listContacts": ("contacts", "list"),
    "createContact": ("contacts", "create"),
    "getContact": ("contacts", "get"),
    "updateContact": ("contacts", "update"),
    "deleteContact": ("contacts", "delete"),
    "importContacts": ("contacts", "import_contacts"),
    "listContactGroups": ("contact_groups", "list"),
    "createContactGroup": ("contact_groups", "create"),
    "getContactGroup": ("contact_groups", "get"),
    "updateContactGroup": ("contact_groups", "update"),
    "deleteContactGroup": ("contact_groups", "delete"),
    "listMailings": ("mailings", "list"),
    "createMailing": ("mailings", "create"),
    "createSmsMailing": ("mailings", "create_sms"),
    "createCallMailing": ("mailings", "create_call"),
    "getMailing": ("mailings", "get"),
    "updateMailing": ("mailings", "update"),
    "deleteMailing": ("mailings", "delete"),
    "listRedirections": ("redirections", "list"),
    "createRedirection": ("redirections", "create"),
    "getRedirection": ("redirections", "get"),
    "updateRedirection": ("redirections", "update"),
    "deleteRedirection": ("redirections", "delete"),
    "listCallScenarios": ("call_scenarios", "list"),
    "createCallScenario": ("call_scenarios", "create"),
    "getCallScenario": ("call_scenarios", "get"),
    "updateCallScenario": ("call_scenarios", "update"),
    "deleteCallScenario": ("call_scenarios", "delete"),
    "retryCallScenario": ("call_scenarios", "retry"),
    "listFollowUpSmsSettings": ("follow_up_sms_settings", "list"),
    "createFollowUpSmsSetting": ("follow_up_sms_settings", "create"),
    "getFollowUpSmsSetting": ("follow_up_sms_settings", "get"),
    "updateFollowUpSmsSetting": ("follow_up_sms_settings", "update"),
    "deleteFollowUpSmsSetting": ("follow_up_sms_settings", "delete"),
    "enableDonglePublicVpn": ("public_vpn", "enable"),
    "disableDonglePublicVpn": ("public_vpn", "disable"),
    "refreshDonglePublicVpnPassword": ("public_vpn", "refresh_password"),
    "listPublicVpnSessions": ("public_vpn", "list_sessions"),
    "listDongleSocksProxies": ("socks_proxies", "list"),
    "createDongleSocksProxy": ("socks_proxies", "create"),
    "getDongleSocksProxy": ("socks_proxies", "get"),
    "updateDongleSocksProxy": ("socks_proxies", "update"),
    "deleteDongleSocksProxy": ("socks_proxies", "delete"),
    "listSipUsers": ("sip_users", "list"),
    "getSipUser": ("sip_users", "get"),
    "getFile": ("files", "download"),
    "getTmpFile": ("files", "download_tmp"),
    "uploadTmpFile": ("files", "upload_tmp"),
    "generateSpeech": ("files", "generate_speech"),
}

# Body fields whose name clashes with a path parameter: (operationId, field) -> Python argument name.
BODY_RENAMES: Dict[Tuple[str, str], str] = {("updateSms", "dongle_id"): "new_dongle_id"}

# Names of models built from inline objects in response wrappers.
WRAPPER_MODEL_NAMES: Dict[str, str] = {"ContactImportResponse": "ContactImportResult"}

# Enum member names the description parser can't derive well.
ENUM_MEMBER_OVERRIDES: Dict[str, Dict[int, str]] = {
    "SmsStatus": {1: "SENT"},
    "DurationPreset": {
        1: "LESS_THAN_1_MINUTE",
        2: "FROM_1_TO_3_MINUTES",
        3: "FROM_3_TO_5_MINUTES",
        4: "MORE_THAN_5_MINUTES",
    },
}

HTTP_METHODS = ("get", "post", "put", "patch", "delete")
RESERVED_ARGS = {"self", "extra_headers", "extra_query", "extra_body", "timeout"}
BASEMODEL_ATTRS = set(dir(pydantic.BaseModel))

spec: Dict[str, Any] = yaml.safe_load(SPEC_PATH.read_text())
SCHEMAS: Dict[str, Any] = spec["components"]["schemas"]


# --------------------------------------------------------------------------------------------- helpers


def ref_name(schema: Dict[str, Any]) -> str:
    return str(schema["$ref"]).split("/")[-1]


def single_ref(schema: Dict[str, Any]) -> Optional[str]:
    if "$ref" in schema:
        return ref_name(schema)
    all_of = schema.get("allOf")
    if isinstance(all_of, list) and len(all_of) == 1 and "$ref" in all_of[0]:
        return ref_name(all_of[0])
    return None


def pascal(name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in re.split(r"[^0-9a-zA-Z]+", name) if part)


def py_name(name: str) -> str:
    out = re.sub(r"[^0-9a-zA-Z_]", "_", name.replace("[]", ""))
    if keyword.iskeyword(out) or out[:1].isdigit():
        out += "_"
    return out


def doc_text(text: Optional[str]) -> str:
    return (text or "").replace("\\", "\\\\").replace('"""', '\\"\\"\\"').strip()


def wrap(text: str, indent: str, width: int = 110) -> List[str]:
    lines: List[str] = []
    for para in text.split("\n"):
        if not para.strip():
            lines.append("")
            continue
        lines.extend(textwrap.wrap(para, width=width, initial_indent=indent, subsequent_indent=indent) or [indent])
    return lines


def docstring(text: str, indent: str) -> List[str]:
    body = doc_text(text)
    if not body:
        return []
    lines = wrap(body, indent)
    if len(lines) == 1 and len(lines[0]) + 6 <= 118:
        return [f'{indent}"""{lines[0].strip()}"""']
    return [f'{indent}"""'] + lines + [f'{indent}"""']


def is_datetime_string(schema: Dict[str, Any], field_name: str) -> bool:
    if schema.get("type") != "string":
        return False
    if schema.get("format") == "date-time":
        return True
    pattern = schema.get("pattern") or ""
    if r"\d{2}:\d{2}:\d{2}" in pattern:
        return True
    return field_name.endswith("_at") and "enum" not in schema


# --------------------------------------------------------------------------------------------- enums

ENUM_CLASSES: Dict[str, str] = {}  # component name -> class name
ENUM_SIGNATURES: Dict[Tuple[Tuple[Any, ...], str], str] = {}  # (values, description) -> class name
ENUM_DEFS: List[Tuple[str, str, List[Tuple[str, int, str]]]] = []


def normalize_enum_description(text: str) -> str:
    return re.sub(r"\s*Null when not set\.?\s*$", "", (text or "").strip()).strip().rstrip(" .")


def parse_enum_members(component: str, schema: Dict[str, Any]) -> List[Tuple[str, int, str]]:
    description = schema.get("description") or ""
    parts = re.split(r"(?:^|[,;]\s*)(\d+):\s*", description)
    labels: Dict[int, str] = {}
    for i in range(1, len(parts) - 1, 2):
        labels[int(parts[i])] = parts[i + 1].strip().rstrip(".,;")
    members: List[Tuple[str, int, str]] = []
    used: set[str] = set()
    overrides = ENUM_MEMBER_OVERRIDES.get(component, {})
    for value in schema["enum"]:
        label = labels.get(value, f"VALUE_{value}")
        name = overrides.get(value)
        if name is None:
            short = re.split(r" \(| - |, |; ", label)[0]
            name = re.sub(r"[^0-9A-Za-z]+", "_", short).strip("_").upper() or f"VALUE_{value}"
            if name[0].isdigit():
                name = f"VALUE_{name}"
        if name in used:
            name = f"{name}_{value}"
        used.add(name)
        members.append((name, value, label))
    return members


for comp_name, comp in SCHEMAS.items():
    if "enum" in comp and comp.get("type") == "integer":
        cls = comp_name[:-4] if comp_name.endswith("Enum") else comp_name
        ENUM_CLASSES[comp_name] = cls
        ENUM_SIGNATURES[(tuple(comp["enum"]), normalize_enum_description(comp.get("description", "")))] = cls
        ENUM_DEFS.append((cls, comp.get("description", ""), parse_enum_members(comp_name, comp)))


def inline_enum_class(schema: Dict[str, Any]) -> Optional[str]:
    key = (tuple(schema.get("enum", [])), normalize_enum_description(schema.get("description", "")))
    return ENUM_SIGNATURES.get(key)


# --------------------------------------------------------------------------------------------- models


@dataclass
class ModelField:
    name: str
    alias: Optional[str]
    type_: str
    required: bool
    nullable: bool
    description: str


@dataclass
class ModelDef:
    name: str
    description: str
    fields: List[ModelField] = field(default_factory=list)


MODELS: Dict[str, ModelDef] = {}
MODEL_QUEUE: List[Tuple[str, Dict[str, Any]]] = []


def model_type(schema: Dict[str, Any], owner: str, field_name: str) -> str:
    ref = single_ref(schema)
    if ref is not None:
        if ref in ENUM_CLASSES:
            return ENUM_CLASSES[ref]
        ensure_model(ref, SCHEMAS[ref])
        return ref
    kind = schema.get("type")
    if kind == "integer":
        if "enum" in schema:
            return inline_enum_class(schema) or "int"
        return "int"
    if kind == "number":
        return "float"
    if kind == "boolean":
        return "bool"
    if kind == "string":
        if schema.get("format") == "binary":
            return "bytes"
        if is_datetime_string(schema, field_name):
            return "datetime.datetime"
        return "str"
    if kind == "array":
        items = schema.get("items") or {}
        return f"List[{model_type(items, owner, field_name)}]"
    if "properties" in schema:
        name = owner + pascal(field_name)
        ensure_model(name, schema)
        return name
    if kind == "object" or "additionalProperties" in schema:
        return "Dict[str, Any]"
    return "Any"


def ensure_model(name: str, schema: Dict[str, Any]) -> None:
    if name in MODELS:
        return
    model = ModelDef(name=name, description=schema.get("description", ""))
    MODELS[name] = model
    required = set(schema.get("required", []))
    for prop, prop_schema in (schema.get("properties") or {}).items():
        attr = py_name(prop)
        alias = None
        if attr in BASEMODEL_ATTRS or attr != prop:
            attr = attr.rstrip("_") + "_"
            alias = prop
        nullable = bool(prop_schema.get("nullable"))
        model.fields.append(
            ModelField(
                name=attr,
                alias=alias,
                type_=model_type(prop_schema, name, prop),
                required=prop in required,
                nullable=nullable,
                description=prop_schema.get("description", ""),
            )
        )


# --------------------------------------------------------------------------------------------- params


PARAMS: Dict[str, Tuple[str, List[Tuple[str, str, bool, str]]]] = {}


def param_type(schema: Dict[str, Any], field_name: str, *, in_method: bool) -> str:
    ref = single_ref(schema)
    if ref is not None:
        if ref in ENUM_CLASSES:
            out = "int"
        else:
            ensure_param(ref)
            out = f"_params.{ref}Param" if in_method else f"{ref}Param"
    else:
        kind = schema.get("type")
        if kind == "integer":
            out = "int"
        elif kind == "number":
            out = "float"
        elif kind == "boolean":
            out = "bool"
        elif kind == "string":
            if "enum" in schema:
                out = "Literal[" + ", ".join(repr(v) for v in schema["enum"]) + "]"
            elif schema.get("format") == "binary":
                out = "bytes"
            elif is_datetime_string(schema, field_name):
                out = "Union[str, datetime.datetime]"
            else:
                out = "str"
        elif kind == "array":
            inner = param_type(schema.get("items") or {}, field_name, in_method=in_method)
            out = f"Iterable[{inner}]" if in_method else f"List[{inner}]"
        elif kind == "object" or "properties" in schema or "additionalProperties" in schema:
            out = "Dict[str, object]"
        else:
            out = "object"
    if schema.get("nullable"):
        out = f"Optional[{out}]"
    return out


def ensure_param(name: str) -> None:
    if name in PARAMS:
        return
    schema = SCHEMAS[name]
    PARAMS[name] = (schema.get("description", ""), [])
    if "properties" not in schema:
        return
    required = set(schema.get("required", []))
    fields = PARAMS[name][1]
    for prop, prop_schema in schema["properties"].items():
        fields.append(
            (prop, param_type(prop_schema, prop, in_method=False), prop in required, prop_schema.get("description", ""))
        )


# --------------------------------------------------------------------------------------------- operations


@dataclass
class Arg:
    wire: str
    name: str
    type_: str
    required: bool
    description: str
    location: str  # path | query | body
    keep_slashes: bool = False
    default: Optional[str] = None


@dataclass
class Operation:
    op_id: str
    resource: str
    method_name: str
    http_method: str
    path: str
    summary: str
    description: str
    args: List[Arg]
    has_body: bool
    kind: str  # page | list_data | list_key | model | result | status | none | bytes
    return_type: str
    item_key: Optional[str] = None
    item_type: Optional[str] = None
    error_codes: List[str] = field(default_factory=list)


def resolve(schema: Dict[str, Any]) -> Dict[str, Any]:
    ref = single_ref(schema)
    return SCHEMAS[ref] if ref is not None and "properties" not in schema else schema


def analyze_response(op: Dict[str, Any], query_names: List[str]) -> Tuple[str, str, Optional[str], Optional[str]]:
    responses = op["responses"]
    success = next(code for code in responses if str(code).startswith("2"))
    content = responses[success].get("content") or {}
    if "application/json" not in content:
        return "bytes", "bytes", None, None
    wrapper_schema = content["application/json"]["schema"]
    wrapper_name = single_ref(wrapper_schema) or op["operationId"][0].upper() + op["operationId"][1:] + "Response"
    wrapper = resolve(wrapper_schema)
    data = (wrapper.get("properties") or {}).get("data") or {}
    base = WRAPPER_MODEL_NAMES.get(wrapper_name, re.sub(r"Response$", "", wrapper_name))

    if wrapper_name == "StatusResponse":
        return "status", "bool", None, None
    if wrapper_name == "NullDataResponse" or (
        data.get("type") == "object" and not data.get("properties") and single_ref(data) is None
    ):
        return "none", "None", None, None
    if data.get("type") == "array":
        item = model_type(data.get("items") or {}, base, "item")
        return "list_data", f"List[{item}]", None, item
    ref = single_ref(data)
    if ref is not None:
        return "model", model_type(data, base, "data"), None, None
    props = data.get("properties") or {}
    arrays = [k for k, v in props.items() if v.get("type") == "array"]
    if len(arrays) == 1 and set(props) <= {arrays[0], "total_count"}:
        key = arrays[0]
        item = model_type(props[key].get("items") or {}, base, key)
        if "page" in query_names:
            return "page", f"Page[{item}]", key, item
        return "list_key", f"List[{item}]", key, item
    if set(props) == {"result"}:
        result_schema = props["result"]
        if single_ref(result_schema) is not None:
            return "result", model_type(result_schema, base, "result"), None, None
        ensure_model(base, result_schema)
        return "result", base, None, None
    ensure_model(base, data)
    return "model", base, None, None


OPS: List[Operation] = []

for path, path_item in spec["paths"].items():
    for http_method, op in path_item.items():
        if http_method not in HTTP_METHODS:
            continue
        op_id = op["operationId"]
        if op_id not in OPERATIONS:
            sys.exit(f"operationId {op_id} ({http_method.upper()} {path}) is not mapped in OPERATIONS")
        resource, method_name = OPERATIONS[op_id]
        params = list(path_item.get("parameters", [])) + list(op.get("parameters", []))
        args: List[Arg] = []
        path_names = re.findall(r"\{([^}]+)\}", path)
        by_name = {p["name"]: p for p in params if p["in"] == "path"}
        for name in path_names:
            p = by_name[name]
            schema = p.get("schema") or {}
            args.append(
                Arg(
                    wire=name,
                    name=py_name(name),
                    type_="int" if schema.get("type") == "integer" else "str",
                    required=True,
                    description=p.get("description", ""),
                    location="path",
                    keep_slashes="/" in (schema.get("pattern") or ""),
                )
            )
        query_names: List[str] = []
        for p in params:
            if p["in"] != "query":
                continue
            query_names.append(p["name"])
            args.append(
                Arg(
                    wire=p["name"],
                    name=py_name(p["name"]),
                    type_=param_type(p.get("schema") or {}, p["name"], in_method=True),
                    required=bool(p.get("required")),
                    description=p.get("description", ""),
                    location="query",
                )
            )
        has_body = False
        body = (op.get("requestBody") or {}).get("content", {}).get("application/json", {}).get("schema")
        if body:
            has_body = True
            body_schema = resolve(body)
            required = set(body_schema.get("required", []))
            for prop, prop_schema in (body_schema.get("properties") or {}).items():
                name = BODY_RENAMES.get((op_id, prop), py_name(prop))
                if name in {a.name for a in args}:
                    sys.exit(f"{op_id}: body field {prop} clashes with a parameter; add it to BODY_RENAMES")
                enum_values = prop_schema.get("enum")
                default = repr(enum_values[0]) if prop in required and enum_values and len(enum_values) == 1 else None
                args.append(
                    Arg(
                        wire=prop,
                        name=name,
                        type_=param_type(prop_schema, prop, in_method=True),
                        required=prop in required and default is None,
                        description=prop_schema.get("description", ""),
                        location="body",
                        default=default,
                    )
                )
        for a in args:
            if a.name in RESERVED_ARGS:
                sys.exit(f"{op_id}: argument {a.name} clashes with a reserved argument")
        kind, return_type, item_key, item_type = analyze_response(op, query_names)
        OPS.append(
            Operation(
                op_id=op_id,
                resource=resource,
                method_name=method_name,
                http_method=http_method.upper(),
                path=path,
                summary=op.get("summary", ""),
                description=op.get("description", ""),
                args=args,
                has_body=has_body,
                kind=kind,
                return_type=return_type,
                item_key=item_key,
                item_type=item_type,
                error_codes=list(op.get("x-error-codes") or []),
            )
        )

missing = set(OPERATIONS) - {o.op_id for o in OPS}
if missing:
    sys.exit(f"OPERATIONS lists unknown operationIds: {sorted(missing)}")


# --------------------------------------------------------------------------------------------- emit: types


def emit_enums() -> str:
    out = [HEADER, "from __future__ import annotations", "", "import enum", ""]
    out.append("__all__ = [" + ", ".join(repr(name) for name, _, _ in ENUM_DEFS) + "]")
    for cls, description, members in ENUM_DEFS:
        out += ["", "", f"class {cls}(enum.IntEnum):"]
        out += docstring(description or cls, "    ")
        out.append("")
        for name, value, label in members:
            out.append(f"    {name} = {value}")
            out += docstring(label, "    ")
    return "\n".join(out) + "\n"


def field_annotation(f: ModelField) -> str:
    type_ = f.type_
    if f.nullable or not f.required:
        type_ = f"Optional[{type_}]"
    line = f"    {f.name}: {type_}"
    if f.alias:
        default = "None, " if (f.nullable or not f.required) else ""
        line += f" = Field({default}alias={f.alias!r})"
    elif not f.required:
        line += " = None"
    return line


def emit_models() -> str:
    names = sorted(MODELS)
    enum_names = [cls for cls, _, _ in ENUM_DEFS]
    out = [
        HEADER,
        "from __future__ import annotations",
        "",
        "import datetime",
        "from typing import Any, Dict, List, Optional",
        "",
        "from pydantic import Field",
        "",
        "from .._models import BaseModel",
        "from .enums import " + ", ".join(sorted(enum_names)),
        "",
        "__all__ = [" + ", ".join(repr(n) for n in names) + "]",
    ]
    for name in names:
        model = MODELS[name]
        out += ["", "", f"class {name}(BaseModel):"]
        out += docstring(model.description, "    ")
        if not model.fields:
            out.append("    pass")
            continue
        if model.description:
            out.append("")
        for f in model.fields:
            out.append(field_annotation(f))
            out += docstring(f.description, "    ")
            out.append("")
        if out[-1] == "":
            out.pop()
    out += ["", "", "for _model in (" + ", ".join(names) + ",):", "    _model.model_rebuild()"]
    return "\n".join(out) + "\n"


def emit_params() -> str:
    names = sorted(PARAMS)
    out: List[str] = []
    for name in names:
        description, fields = PARAMS[name]
        out += ["", "", f"class {name}Param(TypedDict, total=False):"]
        out += docstring(description, "    ")
        if not fields:
            out.append("    pass")
            continue
        if description:
            out.append("")
        for prop, type_, required, desc in fields:
            out.append(f"    {prop}: {'Required[' + type_ + ']' if required else type_}")
            out += docstring(desc, "    ")
            out.append("")
        if out[-1] == "":
            out.pop()
    body = "\n".join(out)
    typing_names = [n for n in ("Dict", "List", "Optional", "Union") if f"{n}[" in body]
    ext_names = [n for n in ("Literal", "Required") if f"{n}[" in body] + ["TypedDict"]
    head = [HEADER, "from __future__ import annotations", ""]
    if "datetime." in body:
        head.append("import datetime")
    if typing_names:
        head.append("from typing import " + ", ".join(typing_names))
    if len(head) > 3:
        head.append("")
    head.append("from typing_extensions import " + ", ".join(ext_names))
    head += ["", "__all__ = [" + ", ".join(repr(f"{n}Param") for n in names) + "]"]
    return "\n".join(head) + "\n" + body + "\n"


def emit_types_init() -> str:
    enum_names = sorted(cls for cls, _, _ in ENUM_DEFS)
    model_names = sorted(MODELS)
    param_names = sorted(f"{n}Param" for n in PARAMS)
    out = [HEADER, "from __future__ import annotations", ""]
    out.append("from .enums import " + ", ".join(enum_names))
    out.append("from .models import " + ", ".join(model_names))
    out.append("from .params import " + ", ".join(param_names))
    out.append("")
    out.append("__all__ = [")
    for n in enum_names + model_names + param_names:
        out.append(f"    {n!r},")
    out.append("]")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------------------------- emit: resources


def arg_annotation(a: Arg) -> str:
    if a.location == "path":
        return f"{a.name}: {a.type_}"
    if a.required:
        return f"{a.name}: {a.type_}"
    if a.default is not None:
        return f"{a.name}: {a.type_} = {a.default}"
    type_ = a.type_
    if type_.startswith("Optional[") and type_.endswith("]"):
        inner = type_[len("Optional[") : -1]
        if inner.startswith("Union[") and inner.endswith("]"):
            inner = inner[len("Union[") : -1]
        return f"{a.name}: Union[{inner}, None, NotGiven] = NOT_GIVEN"
    if type_.startswith("Union[") and type_.endswith("]"):
        return f"{a.name}: Union[{type_[len('Union[') : -1]}, NotGiven] = NOT_GIVEN"
    return f"{a.name}: Union[{type_}, NotGiven] = NOT_GIVEN"


def path_expr(op: Operation) -> str:
    expr = op.path
    for a in op.args:
        if a.location == "path":
            call = f"path_param({a.name}, keep_slashes=True)" if a.keep_slashes else f"path_param({a.name})"
            expr = expr.replace("{" + a.wire + "}", "{" + call + "}")
    return f'f"{expr}"' if "{" in expr else f'"{expr}"'


def method_doc(op: Operation) -> List[str]:
    parts = [op.summary.rstrip(".") + "." if op.summary else ""]
    if op.description and op.description.strip() != op.summary.strip():
        parts += ["", op.description]
    arg_lines: List[str] = []
    for a in op.args:
        if a.description:
            text = doc_text(a.description)
            wrapped = textwrap.wrap(f"{a.name}: {text}", width=104, subsequent_indent="              ")
            arg_lines += ["          " + w if i == 0 else "  " + w for i, w in enumerate(wrapped)]
    body = [doc_text(p) for p in parts]
    out = ['        """']
    for para in body:
        out += wrap(para, "        ") if para else [""]
    if arg_lines:
        out += ["", "        Args:"] + arg_lines
    if op.error_codes:
        out += [""] + wrap("Error codes (``error_message``): " + ", ".join(op.error_codes) + ".", "        ")
    out.append('        """')
    return out


def method_lines(op: Operation, is_async: bool) -> List[str]:
    page_cls = "AsyncPage" if is_async else "SyncPage"
    return_type = op.return_type.replace("Page[", f"{page_cls}[")
    positional = [a for a in op.args if a.location == "path"]
    keyword_args = [a for a in op.args if a.location != "path"]
    keyword_args.sort(key=lambda a: 0 if a.required else 1)
    sig = ["        self,"]
    sig += [f"        {arg_annotation(a)}," for a in positional]
    sig.append("        *,")
    sig += [f"        {arg_annotation(a)}," for a in keyword_args]
    sig += [
        "        extra_headers: Optional[Headers] = None,",
        "        extra_query: Optional[Query] = None,",
    ]
    if op.has_body:
        sig.append("        extra_body: Optional[Body] = None,")
    sig.append("        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,")

    defn = "async def" if is_async else "def"
    out = [f"    {defn} {op.method_name}(", *sig, f"    ) -> {return_type}:"]
    out += method_doc(op)

    aw = "await " if is_async else ""
    query = [a for a in op.args if a.location == "query"]
    body = [a for a in op.args if a.location == "body"]
    query_expr = "{" + ", ".join(f"{a.wire!r}: {a.name}" for a in query) + "}" if query else None
    body_expr = "{" + ", ".join(f"{a.wire!r}: {a.name}" for a in body) + "}" if op.has_body else None
    common = ["extra_headers=extra_headers", "extra_query=extra_query"]
    if op.has_body:
        common.append("extra_body=extra_body")
    common.append("timeout=timeout")

    if op.kind == "page":
        out.append(f"        return {aw}self._client._get_page(")
        out.append(f"            {path_expr(op)},")
        out.append(f"            query={query_expr or '{}'},")
        out.append(f"            item_key={op.item_key!r},")
        out.append(f"            item_type={op.item_type},")
        out += [f"            {c}," for c in common if not c.startswith("extra_body")]
        out.append("        )")
        return out
    if op.kind == "bytes":
        out.append(f"        return {aw}self._client._request_bytes(")
        out.append(f"            {op.http_method!r},")
        out.append(f"            {path_expr(op)},")
        out += [f"            {c}," for c in common]
        out.append("        )")
        return out

    assign = "" if op.kind == "none" else "data = "
    out.append(f"        {assign}{aw}self._client._request(")
    out.append(f"            {op.http_method!r},")
    out.append(f"            {path_expr(op)},")
    if query_expr:
        out.append(f"            query={query_expr},")
    if body_expr:
        out.append(f"            body={body_expr},")
    out += [f"            {c}," for c in common]
    out.append("        )")
    if op.kind == "status":
        out.append('        return bool(isinstance(data, dict) and data.get("status"))')
    elif op.kind == "none":
        out.append("        return None")
    elif op.kind == "list_data":
        out.append(
            f"        return cast({return_type}, construct_type({return_type}, data if isinstance(data, list) else []))"
        )
    elif op.kind == "list_key":
        out.append(f"        items = data.get({op.item_key!r}) if isinstance(data, dict) else data")
        out.append(
            f"        return cast({return_type}, construct_type({return_type}, items if isinstance(items, list) else []))"
        )
    elif op.kind == "result":
        out.append('        result = data.get("result") if isinstance(data, dict) else data')
        out.append(f"        return cast({return_type}, construct_type({return_type}, result))")
    else:
        out.append(f"        return cast({return_type}, construct_type({return_type}, data))")
    return out


def emit_resource(attr: str) -> str:
    stem, tag = RESOURCES[attr]
    ops = [o for o in OPS if o.resource == attr]
    tag_desc = next((t.get("description", "") for t in spec.get("tags", []) if t["name"] == tag), "")
    used_models = set()
    for o in ops:
        for name in re.findall(r"[A-Z][A-Za-z0-9]+", o.return_type):
            if name in MODELS or name in {c for c, _, _ in ENUM_DEFS}:
                used_models.add(name)
    text_all = " ".join(a.type_ for o in ops for a in o.args)
    imports = [
        HEADER,
        "from __future__ import annotations",
        "",
    ]
    if "datetime." in text_all:
        imports.append("import datetime")
    typing_names = {"Optional", "Union"}
    for name in ("Dict", "Iterable", "List"):
        if re.search(rf"\b{name}\[", text_all + " " + " ".join(o.return_type for o in ops)):
            typing_names.add(name)
    if any(o.kind not in ("page", "bytes", "status", "none") for o in ops):
        typing_names.add("cast")
    imports.append("from typing import " + ", ".join(sorted(typing_names, key=str.lower)))
    if "Literal[" in text_all:
        imports += ["", "from typing_extensions import Literal"]
    imports.append("")
    if any(o.kind not in ("page", "bytes", "status", "none") for o in ops):
        imports.append("from .._models import construct_type")
    if any(o.kind == "page" for o in ops):
        imports.append("from .._pagination import AsyncPage, SyncPage")
    imports.append("from .._resource import AsyncAPIResource, SyncAPIResource")
    imports.append("from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout")
    if any(a.location == "path" for o in ops for a in o.args):
        imports.append("from .._utils import path_param")
    if "_params." in text_all:
        imports.append("from ..types import params as _params")
    if used_models:
        imports.append("from ..types import " + ", ".join(sorted(used_models)))
    imports += ["", f"__all__ = [{stem + 'Resource'!r}, {'Async' + stem + 'Resource'!r}]"]

    out = imports
    for is_async in (False, True):
        cls = ("Async" if is_async else "") + stem + "Resource"
        base = "AsyncAPIResource" if is_async else "SyncAPIResource"
        out += ["", "", f"class {cls}({base}):"]
        out += docstring(tag_desc, "    ")
        for o in ops:
            out.append("")
            out += method_lines(o, is_async)
    body = "\n".join(out) + "\n"
    if "Body" not in body.split("__all__", 1)[1]:
        body = body.replace("NOT_GIVEN, Body, Headers", "NOT_GIVEN, Headers")
    return body


def emit_resources_init() -> str:
    out = [
        HEADER,
        "from __future__ import annotations",
        "",
        "from functools import cached_property",
        "from typing import TYPE_CHECKING, Any, cast",
        "",
    ]
    for attr, (stem, _) in RESOURCES.items():
        out.append(f"from .{attr} import Async{stem}Resource, {stem}Resource")
    out += ["", "if TYPE_CHECKING:", "    from .._base_client import AsyncAPIClient, SyncAPIClient", ""]
    exported = []
    for attr, (stem, _) in RESOURCES.items():
        exported += [f"{stem}Resource", f"Async{stem}Resource"]
    out.append("__all__ = [" + ", ".join(repr(n) for n in ["SyncResources", "AsyncResources", *exported]) + "]")
    for is_async in (False, True):
        cls = "AsyncResources" if is_async else "SyncResources"
        client_type = "AsyncAPIClient" if is_async else "SyncAPIClient"
        out += ["", "", f"class {cls}:", '    """Resource groups of the client."""']
        for attr, (stem, tag) in RESOURCES.items():
            rcls = ("Async" if is_async else "") + stem + "Resource"
            tag_desc = next((t.get("description", "") for t in spec.get("tags", []) if t["name"] == tag), "")
            out += ["", "    @cached_property", f"    def {attr}(self) -> {rcls}:"]
            out += docstring(tag_desc, "        ")
            out.append(f'        return {rcls}(cast("{client_type}", cast(Any, self)))')
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------------------------- emit: api.md


def emit_api_md() -> str:
    out = [
        "# API reference",
        "",
        "Every method of `Teleleo` and `AsyncTeleleo`, generated from [`spec/openapi.yaml`](spec/openapi.yaml). "
        "`AsyncTeleleo` has the same methods; they are coroutines and return `AsyncPage` instead of `SyncPage`.",
        "",
        "Models and enums are importable from `teleleo.types`.",
    ]
    for attr, (stem, tag) in RESOURCES.items():
        tag_desc = next((t.get("description", "") for t in spec.get("tags", []) if t["name"] == tag), "")
        out += [
            "",
            f"## `client.{attr}`",
            "",
            tag_desc,
            "",
            "| Method | HTTP | Returns | Description |",
            "|---|---|---|---|",
        ]
        for o in [o for o in OPS if o.resource == attr]:
            args = [a.name for a in o.args if a.location == "path"] + [
                f"{a.name}=…" for a in o.args if a.location != "path" and a.required
            ]
            if any(a.location != "path" and not a.required for a in o.args):
                args.append("**params")
            ret = o.return_type.replace("Page[", "SyncPage[")
            out.append(f"| `{o.method_name}({', '.join(args)})` | `{o.http_method} {o.path}` | `{ret}` | {o.summary} |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------------------------- emit: tests


def sample_for(type_: str) -> str:
    t = type_
    if t.startswith("Optional["):
        t = t[len("Optional[") : -1]
    if t.startswith("Iterable[") or t.startswith("List["):
        return "[" + sample_for(t[t.index("[") + 1 : -1]) + "]"
    if t.startswith("Literal["):
        return t[len("Literal[") :].split(",")[0].rstrip("]")
    if t == "int":
        return "1"
    if t == "float":
        return "1.5"
    if t == "bool":
        return "True"
    if t == "bytes":
        return "b'x'"
    if t.startswith("Union[str, datetime"):
        return "'2026-01-02 03:04:05'"
    if t.startswith("Dict[") or t.startswith("_params."):
        return "{}"
    return "'x'"


def emit_tests() -> str:
    cases = []
    for idx, o in enumerate(OPS):
        args: List[str] = []
        url_path = o.path
        for a in o.args:
            if a.location != "path":
                continue
            if a.keep_slashes:
                value = "ab/0123456789abcdef0123456789abcdef/greeting.wav"
                args.append(repr(value))
            elif a.type_ == "int":
                value = str(1000 + idx)
                args.append(value)
            else:
                value = f"file{idx}"
                args.append(repr(value))
            url_path = url_path.replace("{" + a.wire + "}", value)
        kwargs = {a.name: sample_for(a.type_) for a in o.args if a.location != "path" and a.required}
        body_keys = [a.wire for a in o.args if a.location == "body" and (a.required or a.default is not None)]
        if o.kind == "page":
            response = f'{{"data": {{"{o.item_key}": [{{}}], "total_count": 1}}}}'
        elif o.kind == "list_data":
            response = '{"data": [{}]}'
        elif o.kind == "list_key":
            response = f'{{"data": {{"{o.item_key}": [{{}}]}}}}'
        elif o.kind == "result":
            response = '{"data": {"result": {}}}'
        elif o.kind == "status":
            response = '{"data": {"status": True}}'
        elif o.kind == "none":
            response = '{"data": None}'
        elif o.kind == "bytes":
            response = "None"
        else:
            response = '{"data": {}}'
        expect = o.item_type if o.kind in ("page", "list_data", "list_key") else o.return_type
        cases.append(
            f"    ({o.resource!r}, {o.method_name!r}, [{', '.join(args)}], {{{', '.join(f'{k!r}: {v}' for k, v in kwargs.items())}}}, "
            f"{o.http_method!r}, {url_path!r}, {response}, {o.kind!r}, {expect!r}, {body_keys!r}),"
        )
    return f'''{HEADER}"""One request per operation of the spec: method, path, auth header, required body fields and the result type."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

import httpx
import pytest
import respx

import teleleo.types as types
from teleleo import AsyncPage, AsyncTeleleo, SyncPage, Teleleo

BASE_URL = "https://api.example.test/react_api"

CASES: List[Any] = [
{chr(10).join(cases)}
]


def _check_result(result: Any, kind: str, expect: str) -> None:
    model = getattr(types, expect, None)
    if kind == "page":
        assert isinstance(result, (SyncPage, AsyncPage))
        assert result.total_count == 1 and len(result.items) == 1
        if model is not None:
            assert isinstance(result.items[0], model)
    elif kind in ("list_data", "list_key"):
        assert isinstance(result, list) and len(result) == 1
        if model is not None:
            assert isinstance(result[0], model)
    elif kind == "status":
        assert result is True
    elif kind == "none":
        assert result is None
    elif kind == "bytes":
        assert result == b"\\x00\\x01"
    elif model is not None:
        assert isinstance(result, model)


def _route(http_method: str, path: str, response: Optional[Dict[str, Any]]) -> respx.Route:
    route = respx.route(method=http_method, host="api.example.test", path="/react_api" + path)
    if response is None:
        return route.mock(return_value=httpx.Response(200, content=b"\\x00\\x01"))
    return route.mock(return_value=httpx.Response(200, json=response))


def _check_request(route: respx.Route, body_keys: List[str]) -> None:
    assert route.call_count == 1
    request = route.calls.last.request
    assert request.headers["auth-key"] == "test-key"
    if body_keys:
        sent = json.loads(request.content)
        assert set(body_keys) <= set(sent)


@pytest.mark.parametrize(
    "resource, method, args, kwargs, http_method, path, response, kind, expect, body_keys",
    CASES,
    ids=[f"{{c[0]}}.{{c[1]}}" for c in CASES],
)
@respx.mock
def test_sync(
    resource: str, method: str, args: List[Any], kwargs: Dict[str, Any], http_method: str, path: str,
    response: Optional[Dict[str, Any]], kind: str, expect: str, body_keys: List[str],
) -> None:
    route = _route(http_method, path, response)
    client = Teleleo(api_key="test-key", base_url=BASE_URL, max_retries=0)
    result = getattr(getattr(client, resource), method)(*args, **kwargs)
    _check_request(route, body_keys)
    _check_result(result, kind, expect)


@pytest.mark.parametrize(
    "resource, method, args, kwargs, http_method, path, response, kind, expect, body_keys",
    CASES,
    ids=[f"{{c[0]}}.{{c[1]}}" for c in CASES],
)
@respx.mock
async def test_async(
    resource: str, method: str, args: List[Any], kwargs: Dict[str, Any], http_method: str, path: str,
    response: Optional[Dict[str, Any]], kind: str, expect: str, body_keys: List[str],
) -> None:
    route = _route(http_method, path, response)
    client = AsyncTeleleo(api_key="test-key", base_url=BASE_URL, max_retries=0)
    result = await getattr(getattr(client, resource), method)(*args, **kwargs)
    _check_request(route, body_keys)
    _check_result(result, kind, expect)


def test_every_operation_is_covered() -> None:
    assert len(CASES) == {len(OPS)}
'''


# --------------------------------------------------------------------------------------------- write


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main() -> None:
    resources_dir = PKG / "resources"
    for old in resources_dir.glob("*.py"):
        old.unlink()
    for attr in RESOURCES:
        write(resources_dir / f"{attr}.py", emit_resource(attr))
    write(resources_dir / "__init__.py", emit_resources_init())
    write(PKG / "types" / "enums.py", emit_enums())
    write(PKG / "types" / "models.py", emit_models())
    write(PKG / "types" / "params.py", emit_params())
    write(PKG / "types" / "__init__.py", emit_types_init())
    write(ROOT / "api.md", emit_api_md())
    write(ROOT / "tests" / "test_operations_generated.py", emit_tests())
    generated = [str(PKG / "resources"), str(PKG / "types"), str(ROOT / "tests" / "test_operations_generated.py")]
    ruff = [sys.executable, "-m", "ruff"]
    subprocess.run([*ruff, "check", "--fix", "--quiet", *generated], check=False)
    subprocess.run([*ruff, "format", "--quiet", *generated], check=True)
    print(f"{len(OPS)} operations, {len(MODELS)} models, {len(ENUM_DEFS)} enums, {len(PARAMS)} param types")


if __name__ == "__main__":
    main()
