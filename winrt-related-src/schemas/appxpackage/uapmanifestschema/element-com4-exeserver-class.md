---
title: com4:Class (in com4:ExeServer)
description: Defines an ExeServer class registration. (in com4:ExeServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in com4:ExeServer)



## Description
Defines an ExeServer class registration.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-exeserver.md">&lt;com4:ExeServer&gt;</a></dt>
<dd>
<b>&lt;com4:Class&gt;</b>
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
<com4:Class     EnableOleDefaultHandler = Boolean.
    ProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    VersionIndependentProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    AutoConvertTo = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    InsertableObject = Boolean.
    ShortDisplayName = A string between 1 and 40 characters in length.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
>

<!-- Child elements -->
  ImplementedCategories
  Conversion
  DataFormats
  MiscStatus
  Verbs
  DefaultIcon
  ToolboxBitmap32
  TypeLib

</com4:Class>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| EnableOleDefaultHandler | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | Boolean.| Yes |
| ProgId | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| VersionIndependentProgId | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| AutoConvertTo | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| InsertableObject | Indicates that this class is insertable. | Boolean.| Yes |
| ShortDisplayName | A short version of the class display name. | A string between 1 and 40 characters in length.| Yes |
| Id | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| DisplayName | A localizable string corresponding to the default value of the CLSID's key. | A string between 1 and 256 characters in length. This string is localizable.| Yes |

## Child Elements

| Element | Description |
| -----------| -------------|
| [ImplementedCategories](element-com4-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com4-conversion.md) | Specifies the formats an application can read and write. |
| [DataFormats](element-com4-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [MiscStatus](element-com4-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com4-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com4-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com4-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [TypeLib](element-com4-class-typelib.md) | A type library for a class or interface. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
