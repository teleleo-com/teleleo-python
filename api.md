# API reference

Every method of `Teleleo` and `AsyncTeleleo`, generated from [`spec/openapi.yaml`](spec/openapi.yaml). `AsyncTeleleo` has the same methods; they are coroutines and return `AsyncPage` instead of `SyncPage`.

Models and enums are importable from `teleleo.types`.

## `client.dongles`

Modems of the account and their commands: reboot, Wi-Fi, Wi-Fi extender, number, network info.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /dongle` | `SyncPage[DongleListItem]` | List modems |
| `reboot(dongle_id)` | `POST /dongle/{dongle_id}/reboot` | `bool` | Reboot modem |
| `enable_wifi(dongle_id)` | `POST /dongle/{dongle_id}/wifi/enable` | `bool` | Enable modem Wi-Fi |
| `disable_wifi(dongle_id)` | `POST /dongle/{dongle_id}/wifi/disable` | `bool` | Disable modem Wi-Fi |
| `set_wifi_credentials(dongle_id, hotspot_name=…, hotspot_password=…)` | `POST /dongle/{dongle_id}/wifi/credentials` | `bool` | Set modem Wi-Fi credentials |
| `enable_wifi_extender(dongle_id, ssid=…, password=…, wifi_extender_mode=…)` | `POST /dongle/{dongle_id}/wifi-extender/enable` | `bool` | Enable Wi-Fi extender |
| `disable_wifi_extender(dongle_id)` | `POST /dongle/{dongle_id}/wifi-extender/disable` | `bool` | Disable Wi-Fi extender |
| `scan_wifi_networks(dongle_id)` | `POST /dongle/{dongle_id}/wifi-extender/networks` | `bool` | Scan Wi-Fi networks |
| `update_offline_notification(dongle_id, is_enabled=…)` | `PUT /dongle/{dongle_id}/setting/offline-notification` | `bool` | Set offline notification |
| `set_number(dongle_id, number=…)` | `PUT /dongle/{dongle_id}/number` | `bool` | Set modem number |
| `get(dongle_id)` | `GET /dongle/{dongle_id}` | `Dongle` | Get modem |
| `update(dongle_id, **params)` | `PUT /dongle/{dongle_id}` | `Dongle` | Update modem |
| `get_network_info(dongle_id)` | `POST /dongle/{dongle_id}/mobile-network-info` | `DongleNetworkInfo` | Get modem network info |
| `get_sim_identifiers(dongle_id)` | `POST /dongle/{dongle_id}/mobile-network-ids` | `DongleSimIdentifiers` | Get modem SIM identifiers |
| `list_statistics(dongle_id, **params)` | `GET /dongle/{dongle_id}/statistic` | `List[DongleStatistic]` | List modem traffic statistics |

## `client.sms`

SMS of the modems: history, sending, replies, threads.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `send(dongle_id, number=…, message=…, **params)` | `POST /dongle/{dongle_id}/outgoing-sms` | `Sms` | Send SMS |
| `send_to_contact(dongle_id, contact_id=…, message=…, **params)` | `POST /dongle/{dongle_id}/outgoing-contact-sms` | `Sms` | Send SMS to contact |
| `reply(dongle_id, replied_to_sms_id=…, message=…, **params)` | `POST /dongle/{dongle_id}/reply-sms` | `Sms` | Reply to SMS |
| `list_threads(**params)` | `GET /sms/thread` | `SyncPage[SmsThread]` | List SMS threads |
| `list(**params)` | `GET /sms` | `SyncPage[Sms]` | List SMS |
| `list_for_dongle(dongle_id, **params)` | `GET /dongle/{dongle_id}/sms` | `SyncPage[Sms]` | List modem SMS |
| `get(dongle_id, sms_id)` | `GET /dongle/{dongle_id}/sms/{sms_id}` | `Sms` | Get SMS |
| `update(dongle_id, sms_id, **params)` | `PUT /dongle/{dongle_id}/sms/{sms_id}` | `Sms` | Update SMS |
| `delete(dongle_id, sms_id)` | `DELETE /dongle/{dongle_id}/sms/{sms_id}` | `None` | Delete SMS |

## `client.calls`

Calls of the modems: history, outgoing calls.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /call` | `SyncPage[Call]` | List calls |
| `create(dongle_id, **params)` | `POST /dongle/{dongle_id}/call` | `Call` | Make call |
| `get(dongle_id, call_id)` | `GET /dongle/{dongle_id}/call/{call_id}` | `Call` | Get call |
| `delete(dongle_id, call_id)` | `DELETE /dongle/{dongle_id}/call/{call_id}` | `None` | Delete call |

## `client.ussd`

USSD requests through a modem.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(dongle_id, **params)` | `GET /dongle/{dongle_id}/ussd` | `SyncPage[Ussd]` | List USSD requests |
| `send(dongle_id, command=…)` | `POST /dongle/{dongle_id}/ussd` | `Ussd` | Send USSD |
| `get(dongle_id, ussd_id)` | `GET /dongle/{dongle_id}/ussd/{ussd_id}` | `Ussd` | Get USSD request |
| `delete(dongle_id, ussd_id)` | `DELETE /dongle/{dongle_id}/ussd/{ussd_id}` | `bool` | Delete USSD request |
| `delete_all(dongle_id)` | `DELETE /dongle/{dongle_id}/ussds` | `bool` | Delete USSD history |

## `client.contacts`

Address book of the account.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /contact` | `SyncPage[Contact]` | List contacts |
| `create(phone=…, name=…, contact_group_ids=…, **params)` | `POST /contact` | `Contact` | Create contact |
| `get(contact_id)` | `GET /contact/{contact_id}` | `Contact` | Get contact |
| `update(contact_id, phone=…, name=…, contact_group_ids=…, **params)` | `PUT /contact/{contact_id}` | `Contact` | Update contact |
| `delete(contact_id)` | `DELETE /contact/{contact_id}` | `bool` | Delete contact |
| `import_contacts(data=…, **params)` | `POST /contact/import` | `ContactImportResult` | Import contacts |

## `client.contact_groups`

Groups of contacts, used by mailings, call scenarios and redirections.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /contact-group` | `SyncPage[ContactGroup]` | List contact groups |
| `create(name=…, contact_ids=…)` | `POST /contact-group` | `ContactGroup` | Create contact group |
| `get(contact_group_id)` | `GET /contact-group/{contact_group_id}` | `ContactGroup` | Get contact group |
| `update(contact_group_id, name=…, contact_ids=…)` | `PUT /contact-group/{contact_group_id}` | `ContactGroup` | Update contact group |
| `delete(contact_group_id)` | `DELETE /contact-group/{contact_group_id}` | `bool` | Delete contact group |

## `client.mailings`

Bulk SMS and call campaigns.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /mailing` | `SyncPage[Mailing]` | List mailings |
| `create(name=…, mailing_type_id=…, mailing_entity_type_id=…, dongle_id=…, **params)` | `POST /mailing` | `Mailing` | Create mailing |
| `create_sms(name=…, text=…, mailing_type_id=…, dongle_id=…, **params)` | `POST /mailing/sms` | `Mailing` | Create SMS mailing |
| `create_call(name=…, mailing_type_id=…, dongle_id=…, **params)` | `POST /mailing/call` | `Mailing` | Create call mailing |
| `get(mailing_id)` | `GET /mailing/{mailing_id}` | `Mailing` | Get mailing |
| `update(mailing_id, **params)` | `PUT /mailing/{mailing_id}` | `Mailing` | Update mailing |
| `delete(mailing_id)` | `DELETE /mailing/{mailing_id}` | `bool` | Delete mailing |

## `client.redirections`

Rules for incoming SMS and calls: forwarding, auto reply, HTTP callback.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /redirection` | `SyncPage[Redirection]` | List redirections |
| `create(condition=…, name=…, params=…, redirection_type_id=…)` | `POST /redirection` | `Redirection` | Create redirection |
| `get(redirection_id)` | `GET /redirection/{redirection_id}` | `Redirection` | Get redirection |
| `update(redirection_id, condition=…, name=…, params=…, redirection_type_id=…)` | `PUT /redirection/{redirection_id}` | `Redirection` | Update redirection |
| `delete(redirection_id)` | `DELETE /redirection/{redirection_id}` | `bool` | Delete redirection |

## `client.call_scenarios`

What a modem plays to incoming callers.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /call-scenario` | `SyncPage[CallScenario]` | List call scenarios |
| `create(name=…, is_call_record=…, dongle_id=…, call_scenario_type_id=…, tmp_file_id=…, **params)` | `POST /call-scenario` | `CallScenario` | Create call scenario |
| `get(call_scenario_id)` | `GET /call-scenario/{call_scenario_id}` | `CallScenario` | Get call scenario |
| `update(call_scenario_id, **params)` | `PUT /call-scenario/{call_scenario_id}` | `CallScenario` | Update call scenario |
| `delete(call_scenario_id)` | `DELETE /call-scenario/{call_scenario_id}` | `bool` | Delete call scenario |
| `retry(call_scenario_id)` | `POST /call-scenario/{call_scenario_id}/retry` | `CallScenario` | Retry call scenario delivery |

## `client.follow_up_sms_settings`

SMS a modem sends to a caller after a call.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /follow-up-sms-setting` | `SyncPage[FollowUpSmsSetting]` | List follow-up SMS settings |
| `create(dongle_id=…, name=…, text=…, **params)` | `POST /follow-up-sms-setting` | `FollowUpSmsSetting` | Create follow-up SMS setting |
| `get(follow_up_sms_setting_id)` | `GET /follow-up-sms-setting/{follow_up_sms_setting_id}` | `FollowUpSmsSetting` | Get follow-up SMS setting |
| `update(follow_up_sms_setting_id, dongle_id=…, name=…, text=…, **params)` | `PUT /follow-up-sms-setting/{follow_up_sms_setting_id}` | `FollowUpSmsSetting` | Update follow-up SMS setting |
| `delete(follow_up_sms_setting_id)` | `DELETE /follow-up-sms-setting/{follow_up_sms_setting_id}` | `bool` | Delete follow-up SMS setting |

## `client.public_vpn`

VPN access through a modem.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `enable(dongle_id)` | `POST /dongle/{dongle_id}/public-vpn/enable` | `bool` | Enable public VPN |
| `disable(dongle_id)` | `POST /dongle/{dongle_id}/public-vpn/disable` | `bool` | Disable public VPN |
| `refresh_password(dongle_id)` | `POST /dongle/{dongle_id}/public-vpn/refresh-password` | `bool` | Refresh public VPN password |
| `list_sessions()` | `GET /public-vpn/connect-session-list` | `List[PublicVpnSession]` | List public VPN sessions |

## `client.socks_proxies`

SOCKS5 proxy through the mobile network of a modem.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /dongle-socks-proxy` | `SyncPage[DongleSocksProxy]` | List SOCKS proxies |
| `create(dongle_id=…, password=…, allowed_ips=…)` | `POST /dongle-socks-proxy` | `DongleSocksProxy` | Create SOCKS proxy |
| `get(dongle_socks_proxy_id)` | `GET /dongle-socks-proxy/{dongle_socks_proxy_id}` | `DongleSocksProxy` | Get SOCKS proxy |
| `update(dongle_socks_proxy_id, password=…, allowed_ips=…)` | `PUT /dongle-socks-proxy/{dongle_socks_proxy_id}` | `DongleSocksProxy` | Update SOCKS proxy |
| `delete(dongle_socks_proxy_id)` | `DELETE /dongle-socks-proxy/{dongle_socks_proxy_id}` | `bool` | Delete SOCKS proxy |

## `client.sip_users`

SIP accounts of the modems.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `list(**params)` | `GET /sip-user` | `List[PbxSipUser]` | List SIP users |
| `get(sip_user_id)` | `GET /sip-user/{sip_user_id}` | `PbxSipUser` | Get SIP user |

## `client.files`

Downloads, temporary audio uploads and text-to-speech.

| Method | HTTP | Returns | Description |
|---|---|---|---|
| `download(file_id)` | `GET /file/{file_id}` | `bytes` | Get file |
| `download_tmp(file_id)` | `GET /file/tmp/{file_id}` | `bytes` | Get temporary file |
| `upload_tmp(file_base64=…, file_name=…, **params)` | `POST /file/upload-tmp` | `TmpFile` | Upload temporary file |
| `generate_speech(text=…, voice=…, language=…)` | `POST /file/generate-speech` | `TmpFile` | Generate speech |
