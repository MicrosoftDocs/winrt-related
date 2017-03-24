---
author: laurenhughes
ms.assetid: 350e2733-4da7-4e0b-a0aa-291c15c80e25
title: rescap3:DesktopAppMigration
description: Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:DesktopAppMigration


## Description
Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-rescap3-extension.md">&lt;rescap3:Extension&gt;</a></dt>
<dd><b>&lt;rescap3:DesktopAppMigration&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<rescap3:DesktopAppMigration AcquisitionUri? = A string between 1 and 2084 characters in length. >
  <!-- Child elements -->
  rescap3:DesktopApp{1,10000}
</rescap3:DesktopAppMigration>
```

### Key
`{}` specific range of occurrences
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| AcquisitionUri | The URI that a tile/pin will be migrated to. | A string between 1 and 2084 characters in length. | No |

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [DesktopApp](element-rescap3-desktopapp.md) | Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3</p></td>
</tr>
</tbody>
</table>