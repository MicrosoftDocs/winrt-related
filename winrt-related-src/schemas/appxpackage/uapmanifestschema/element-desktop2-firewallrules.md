---
author: mcleanbyron
ms.assetid: 62655174-6b4c-4fef-bc99-b5ef22b85333
title: desktop2:FirewallRules
description: Specifies firewall exception rules used by Windows Desktop Bridge apps.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:FirewallRules


## Description
Specifies firewall exception rules used by Windows Desktop Bridge apps.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd><b>&lt;desktop2:FirewallRules&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```sytnax
<desktop2:FirewallRules Executable = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. >

 <!-- Child elements -->
 Rule{0,1000}
</desktop2:FirewallRules>
```
### Key
`{}` specific range of occurrences

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Executable | The application executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | Yes |

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [Rule](element-desktop2-rule.md) | Defines a firewall exception rule. |

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