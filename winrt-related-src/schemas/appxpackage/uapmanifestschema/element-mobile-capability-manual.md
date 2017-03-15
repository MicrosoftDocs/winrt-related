---
Description: Declares a capability required by a package.
MS-HAID: UapManifestSchema.element\_mobile\_capability\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: mobile:Capability (Windows 10)
ms.assetid: c3074580-c334-4578-93e1-e7eb2c58c8ea
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# mobile:Capability (Windows 10)


Declares a capability required by a package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;mobile:Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax


```
<mobile:Capability Name = "recordedCallsFolder"
</mobile:Capability>
```

## Attributes and Elements


**Attributes**

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td>The name of the capability.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>recordedCallsFolder</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                               | Description                                                                |
|----------------------------------------------|----------------------------------------------------------------------------|
| [**Capabilities**](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

 

## Requirements


|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/mobile/windows10 |

 

 

 



