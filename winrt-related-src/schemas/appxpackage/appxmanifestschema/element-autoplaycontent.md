---
Description: Declares an app extensibility point of type windows.autoPlayContent.
Search.Product: eADQiWindows 10XVcnh
title: AutoPlayContent
ms.assetid: 35cf3998-2a45-4ecc-91a5-13d328b0b649


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# AutoPlayContent


Declares an app extensibility point of type **windows.autoPlayContent**. The app provides the specified AutoPlay content actions.

## Element hierarchy

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
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;AutoPlayContent&gt;</b></dd>
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

``` syntax
<AutoPlayContent>

  <!-- Child elements -->
  LaunchAction{1,1000}

</AutoPlayContent>
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
<td><a href="element-launchaction.md">LaunchAction (in type: CT_AutoPlayContent)</a> </td>
<td><p>Describes an AutoPlay content action.</p></td>
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
<td><a href="element-1-extension.md">Extension (in type: CT_ApplicationExtensions)</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When a volume-based device is connected to a computer or a disc is inserted into a CD or DVD drive, the system raises an AutoPlay content event. This extensibility point enables your app to be listed as an AutoPlay choice for one or more AutoPlay content events.

You can use any value for the **Verb** attribute except, **open**, which is reserved.

## Examples

```XML
<Extension Category="windows.autoPlayContent">
  <AutoPlayContent>
    <LaunchAction Verb="show" ActionDisplayName="Show Pictures" ContentEvent="ShowPicturesOnArrival"/>
  </AutoPlayContent>
</Extension>
```

## See also


**Tasks**
[Auto-launching with AutoPlay](https://msdn.microsoft.com/library/windows/apps/hh452731)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><pre>http://schemas.microsoft.com/appx/2010/manifest</pre></td>
</tr>
</tbody>
</table>

 

 



