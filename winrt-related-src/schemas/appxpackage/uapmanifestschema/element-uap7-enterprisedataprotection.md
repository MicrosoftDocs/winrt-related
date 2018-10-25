---
author: laurenhughes
title: uap7:EnterpriseDataProtection
description: When declared in an app, this ensures that all files it creates and clipboard/dragged items are encrypted.
ms.author: lahugh
ms.date: 10/03/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap7:EnterpriseDataProtection

## Description
Declares that the app is safe for auto-encryption and allows it to be managed without device enrollment via Windows Information Protection policy. 

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap7-extension.md">&lt;uap7:Extension&gt;</a></dt>
<dd><b>&lt;uap7:EnterpriseDataProtection&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap7:EnterpriseDataProtection ProtectionMode = One of the following values: auto, default />
```

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ProtectionMode | The mode of data protection. | One of the following values: auto, default | Yes |

### Child Elements
None

## Remarks
Use this extension only if the app is exclusively for work, and/or you provide a mechanism to restore any non-work personal data the app modifies. All files that the app creates or modifies will be encrypted on behalf of the managing organization, and become inaccessible after a selective wipe occurs, when the protection policy is removed from the device. (To safely handle both work and personal data when managed with Windows Information Protection use the enterpriseDataPolicy capability instead.)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/7</p></td>
</tr>
</tbody>
</table>