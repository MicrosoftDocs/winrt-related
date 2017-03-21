---
Description: A property that describes the item.
Search.Product: eADQiWindows 10XVcnh
title: Property
ms.assetid: b5d5075f-7f4f-4c56-8fd6-259f0c78d029
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema
---

# Property


A property that describes the item.

## Element hierarchy

<dl>
<dt><a href="element-Properties.md">&lt;Properties&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-AdditionalProperties.md">&lt;AdditionalProperties&gt;</a></dt>
<dd><b>&lt;Property&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Property Key   = string
          Type? = "bstr" | "boolean" | "string" | "wstr" | "astr" | ... : "string" >

  <!-- Child elements -->
  Value*

  <!-- This element may also contain text (mixed content). -->

</Property>
```

### Key

`?`   optional (zero or one)

`:`   default value

`*`   optional (zero or more)

## Attributes and Elements


### Attributes

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
<td><strong>Key</strong></td>
<td><p>The key that identifies the property. This must be a system property name (see [Windows Properties](https://msdn.microsoft.com/library/windows/desktop/dd561977) for a list) or the [<strong>PROPERTYKEY</strong>](https://msdn.microsoft.com/library/windows/desktop/bb773381) of a property. (You can use the <strong>PROPERTYKEY</strong> to support arbitrary properties that are not known to the system.)</p></td>
<td>string</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td><p>The type of value the property contains.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>bstr</li>
<li>boolean</li>
<li>string</li>
<li>wstr</li>
<li>astr</li>
<li>byte</li>
<li>int16</li>
<li>uint16</li>
<li>int32</li>
<li>uint32</li>
<li>uint64</li>
<li>int64</li>
<li>double</li>
<li>datetime</li>
<li>stringarray</li>
<li>guid</li>
<li>blob</li>
<li>null</li>
<li>empty</li>
</ul></td>
<td>No</td>
<td>string</td>
</tr>
</tbody>
</table>

 

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
<td>[Value](element-value.md)</td>
<td><p>The value that will be indexed for the property.</p></td>
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
<td>[AdditionalProperties](element-additionalproperties.md)</td>
<td><p>Contains additional properties that describe the item.</p></td>
</tr>
</tbody>
</table>

 

## See also


[Indexer sample](http://go.microsoft.com/fwlink/p/?LinkID=311565)

[**Windows.Storage.Search**](https://msdn.microsoft.com/library/windows/apps/br208106)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/Search/2013/ApplicationContent</p></td>
</tr>
</tbody>
</table>

 

 



