---
ms.assetid: 603c4ca9-2407-46f8-9e48-d0663a12ddff
title: desktop2:Rule
description: Defines a firewall exception rule.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:Rule

Defines a firewall exception rule.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-package-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:FirewallRules\>](element-desktop2-firewallrules.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:Rule\>**

## Syntax

```xml
<desktop2:Rule
  Direction = 'A string that can have one of the following values: "in" or "out".'
  IPProtocol = 'A string that can have one of the following values: "ICMPv4", "ICMPv6", "TCP", "UDP", "GRE", "AH", "ESP", "EGP", "GGP", "HMP", "IGMP", "RVD", "OSPFIGP", "PUP", "RDP", or "RSVP".'
  Profile = 'A string that can have one of the following values: "domain", "private", "domainAndPrivate", "public", or "all".'
  LocalPortMin = 'An optional integer with a value between 1 and 65535 (inclusive).'
  LocalPortMax = 'An optional integer with a value between 1 and 65535.'
  RemotePortMin = 'An optional integer with a value between 1 and 65535.'
  RemotePortMax = 'An optional integer with a value between 1 and 65535.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Direction** | The direction of the rule. | A string that can have one of the following values: "in" or "out". | Yes |  |
| **IPProtocol** | The IP protocol for the rule. | A string that can have one of the following values: *ICMPv4*, *ICMPv6*, *TCP*, *UDP*, *GRE*, *AH*, *ESP*, *EGP*, *GGP*, *HMP*, *IGMP*, *RVD*, *OSPFIGP*, *PUP*, *RDP*, or *RSVP*. | Yes |  |
| **Profile** | Thenprofile of the network. | A string that can have one of the following values: *domain*, *private*, *domainAndPrivate*, *public*, or *all*. | Yes |  |
| **LocalPortMin** | A min value for the local port. | An optional integer with a value between 1 and 65535 (inclusive). | No |  |
| **LocalPortMax** | A max value for the local port. | An optional integer with a value between 1 and 65535. | No |  |
| **RemotePortMin** | A min value for the remote port. | An optional integer with a value between 1 and 65535. | No |  |
| **RemotePortMax** | A max value for the remote port. | An optional integer with a value between 1 and 65535. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:FirewallRules](element-desktop2-firewallrules.md) | Specifies firewall exception rules used by Windows Desktop Bridge apps. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
