---
Description: Indicates whether or not the package is multi-user aware. 
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportedUsers (Windows 10)
ms.assetid: 5be5aec1-f253-4e1f-b386-8e9ae815a4e9


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportedUsers (Windows 10)


Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;uap:SupportedUsers&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SupportedUsers>

  "single" | "multiple"

</uap:SupportedUsers>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-properties.md">Properties</a> </td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

## Examples

```XML
    <Properties>
        <uap:SupportedUsers>single</uap:SupportedUsers>
    </Properties>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



