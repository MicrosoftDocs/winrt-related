---
Description: Declares a package extensibility point of type windows.activatableClass.inProcessServer.
Search.Product: eADQiWindows 10XVcnh
title: InProcessServer
ms.assetid: 47e3c888-76eb-4d12-977c-ebd947a2b63c
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# InProcessServer




Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;InProcessServer&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<InProcessServer>

  <!-- Child elements -->
  Path,
  ActivatableClass{1,65535}

</InProcessServer>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[ActivatableClass (type: CT_InProcessActivatableClass)](element-activatableclass.md)</td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="even">
<td>[Path (type: ST_FileName)](element-path.md)</td>
<td><p>The path to the DLL.</p></td>
</tr>
</tbody>
</table>

 

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
<td>[Extension (in type: CT_PackageExtensions)](element-1-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XML
<Extension Category="windows.activatableClass.inProcessServer">
      <InProcessServer>
        <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
        <ActivatableClass ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
      </InProcessServer>
</Extension>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



