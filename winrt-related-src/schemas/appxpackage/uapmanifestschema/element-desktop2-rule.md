---

ms.assetid: 603c4ca9-2407-46f8-9e48-d0663a12ddff
title: desktop2:Rule
description: Defines a firewall exception rule.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:Rule

## Description
Defines a firewall exception rule.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-firewallrules.md">&lt;desktop2:FirewallRules&gt;</a></dt>
<dd><b>&lt;desktop2:Rule&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<desktop2:Rule Direction = One of the following string values: "in", "out"
               IPProtocol = A string value representing the IP protocol. See Attributes table for more details.
               Profile = One of the following string values: "domain", "private", "domainAndPrivate", "public", "all"
               LocalPortMin? = An integer value between 0 and 65535.
               LocalPortMax? = An integer value between 0 and 65535.
               RemotePortMin? = An integer value between 0 and 65535.
               RemotePortMax? = An integer value between 0 and 65535. >
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Direction | The direction for the rule. | One of the following string values: "in", "out" | Yes |
| IPProtocol | The IP protocol for the rule. | These are the supported IP protocols: <ul><li>ICMPv4</li><li>ICMPv6</li><li>TCP</li><li>UDP</li><li>GRE</li><li>AH</li><li>ESP</li><li>EGP</li><li>GGP</li><li>HMP</li><li>IGMP</li><li>RVD</li><li>OSPFIGP</li><li>PUP</li><li>RDP</li><li>RSVP</li></ul> | Yes |
| Profile | The profile of the network. | One of the following string values: <ul><li>domain</li><li>private</li><li>domainAndPrivate</li><li>public</li><li>all</li></ul> | Yes |
| LocalPortMin | A min value for the local port. | An integer value between 0 and 65535. | No |
| LocalPortMax | A max value for the local port. | An integer value between 0 and 65535. | No |
| RemotePortMin | A min value for the remote port. | An integer value between 0 and 65535. | No |
| RemotePortMax | A max value for the remote port. | An integer value between 0 and 65535. | No |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>