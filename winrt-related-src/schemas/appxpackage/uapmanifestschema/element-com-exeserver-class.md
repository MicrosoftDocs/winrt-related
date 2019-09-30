---
author: mcleanbyron
ms.assetid: 50d31c23-2d15-428d-9db1-e8f3441a6541
title: com:Class (in ExeServer)
description: Defines an ExeServer class registration.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:Class (in ExeServer)

## Description
Defines an ExeServer class registration.

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver.md">&lt;com:ExeServer&gt;</a></dt>
<dd><b>&lt;com:Class&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
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
<com:Class
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName? = A string between 1 and 256 characters in length.
    EnableOleDefaultHandler? = Boolean.
    ProgId? = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    VersionIndependentProgId? = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    AutoConvertTo? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    InsertableObject? = Boolean.
    ShortDisplayName? = A string between 1 and 40 characters in length. >

  <!-- Child elements -->
  ( ImplementedCategories?,
  Conversion?,
  DataFormats?,
  MiscStatus?,
  Verbs?,
  DefaultIcon?,
  ToolboxBitmap32? 
  )
</com:Class>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id        | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| DisplayName | A localizable string corresponding to the default value of the CLSID's key. | A string between 1 and 256 characters in length. | No |
| EnableOleDefaultHandler | This should be set to true if the default value of the [InprocHandler32](https://msdn.microsoft.com/library/windows/desktop/ms693485.aspx) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | Boolean. | No |
| ProgId | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |
| VersionIndependentProgId | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |
| AutoConvertTo | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| InsertableObject | Indicates that this class is insertable. | Boolean. | No |
| ShortDisplayName | A short version of the class display name. | A string between 1 and 40 characters in length. | No |

## Child Elements

| Child Element         | Description |
|-----------------------|-------------|
| [ImplementedCategories](element-com-exe-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com-exe-conversion.md) | Specifies the read/write permissions of a class. |
| [DataFormats](element-com-exe-dataformats.md) | Specifies the default and main data formats supported. |
| [MiscStatus](element-com-exe-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com-exe-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com-exe-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com-exe-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |

## Remarks
Each **Class** registered under an **ExeServer** must have an **Id** attribute corresponding to the [CLSID](https://msdn.microsoft.com/library/windows/desktop/ms691424.aspx). 

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>