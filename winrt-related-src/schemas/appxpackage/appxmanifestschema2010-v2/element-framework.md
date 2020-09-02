---
Description: Indicates whether the package is a framework package.
Search.Product: eADQiWindows 10XVcnh
title: Framework
ms.assetid: 2a8e1c58-b079-4ef1-ae62-c27bb3f5a469


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Framework




Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a framework.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;Framework&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Framework>

  boolean

</Framework>
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
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

## Remarks

A package marked as a framework package cannot declare dependencies on other packages.

A framework package cannot define the [**Applications**](../appxmanifestschema/element-applications.md) or [**Capabilities**](appxmanifestschema/../element-capabilities.md) node.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 