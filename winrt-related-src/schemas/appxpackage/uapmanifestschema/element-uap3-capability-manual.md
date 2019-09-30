---
Description: Declares a capability required by a package.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Capability (Windows 10)
ms.assetid: 1a5d687b-4e1f-479a-a24e-eeda24afc560
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Capability (Windows 10)


Declares a capability required by a package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;uap3:Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax


```
<uap3:Capability Name = "backgroundMediaPlayback" | "userNotificationListener"
</uap3:Capability>
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
<li>backgroundMediaPlayback</li>
<li>userNotificationListener</li>
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

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Capabilities>
        <uap3:Capability Name="backgroundMediaPlayback"/>  
        <uap3:Capability Name="userNotificationListener"/>  
    </Capabilities>
</Package>
```

## Requirements


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 



