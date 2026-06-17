---
title: desktop2:Rule
description: Defines a firewall exception rule.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:FirewallRules, desktop2:Rule]
---

# desktop2:Rule

Defines a firewall exception rule.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:FirewallRules>`](element-desktop2-firewallrules.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:Rule>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:FirewallRules>`](element-desktop2-firewallrules.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:Rule>`**

## Syntax

```xml
<desktop2:Rule
  Direction = 'A required string that can have one of the following values: "in", or "out".'
  IPProtocol = 'A required string that can have one of the following values: "ICMPv4", "ICMPv6", "TCP", "UDP", "GRE", "AH", "ESP", "EGP", "GGP", "HMP", "IGMP", "RVD", "OSPFIGP", "PUP", "RDP", or "RSVP".'
  Profile = 'A required string that can have one of the following values: "domain", "private", "domainAndPrivate", "public", or "all".'
  LocalPortMin = 'An optional integer value between 1 and 65535.'
  LocalPortMax = 'An optional integer value between 1 and 65535.'
  RemotePortMin = 'An optional integer value between 1 and 65535.'
  RemotePortMax = 'An optional integer value between 1 and 65535.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Direction** | The direction of the rule. | A string that can have one of the following values: *in*, *out*. | Yes |  |
| **IPProtocol** | The IP protocol for the rule. | A string that can have one of the following values: *ICMPv4*, *ICMPv6*, *TCP*, *UDP*, *GRE*, *AH*, *ESP*, *EGP*, *GGP*, *HMP*, *IGMP*, *RVD*, *OSPFIGP*, *PUP*, *RDP*, *RSVP*. | Yes |  |
| **Profile** | Thenprofile of the network. | A string that can have one of the following values: *domain*, *private*, *domainAndPrivate*, *public*, *all*. | Yes |  |
| **LocalPortMin** | A min value for the local port. | An optional integer value between 1 and 65535. | No |  |
| **LocalPortMax** | A max value for the local port. | An optional integer value between 1 and 65535. | No |  |
| **RemotePortMin** | A min value for the remote port. | An optional integer value between 1 and 65535. | No |  |
| **RemotePortMax** | A max value for the remote port. | An optional integer value between 1 and 65535. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop2:FirewallRules](element-desktop2-firewallrules.md) | Specifies firewall exception rules used by Windows Desktop Bridge apps. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
