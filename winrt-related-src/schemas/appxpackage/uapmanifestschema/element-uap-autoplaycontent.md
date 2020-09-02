---
Description: Declares an app extensibility point of type windows.autoPlayContent.
Search.Product: eADQiWindows 10XVcnh
title: uap:AutoPlayContent (Windows 10)
ms.assetid: 15514696-9195-4dd1-91af-2b97383992cc


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:AutoPlayContent (Windows 10)


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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd><b>&lt;uap:AutoPlayContent&gt;</b></dd>
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
  uap:LaunchAction{1,1000}

</uap:AutoPlayContent>
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
<td><a href="element-uap-launchaction.md">uap:LaunchAction (in type: CT_AutoPlayContent)</a> </td>
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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When a volume-based device is connected to a computer or a disc is inserted into a CD or DVD drive, the system raises an AutoPlay content event. This extensibility point enables your app to be listed as an AutoPlay choice for one or more AutoPlay content events.

You can use any value for the **Verb** attribute except, **open**, which is reserved.

## Examples

```XML
<uap:Extension Category="windows.autoPlayContent">
  <uap:AutoPlayContent>
    <uap:LaunchAction Verb="show" ActionDisplayName="Show Pictures" ContentEvent="ShowPicturesOnArrival"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## See also


**Tasks**
[Auto-launching with AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 