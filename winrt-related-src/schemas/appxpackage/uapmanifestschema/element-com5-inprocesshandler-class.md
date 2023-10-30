---
title: com5:Class (in InProcessHandler)
description: Defines an in-process handler class registration. (in com5:InProcessHandler)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:Class (in InProcessHandler)



## Description

Defines an in-process handler class registration.

## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:Extension\>](element-com4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:ComServer\>](element-com4-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:InProcessHandler\>](element-com5-inprocesshandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:Class&gt;**


## Syntax
```syntax
<com5:Class     Virtualization = "enabled" | "disabled"
    ProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    VersionIndependentProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    AutoConvertTo = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    InsertableObject = Boolean.
    ShortDisplayName = A string between 1 and 40 characters in length.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
>
<!-- Child elements -->
  ImplementedCategories{0,4000}
  Conversion{0,4000}
  DataFormats{0,4000}
  MiscStatus{0,4000}
  Verbs{0,4000}
  DefaultIcon{0,4000}
  ToolboxBitmap32{0,4000}
  TypeLib{0,4000}
</com5:Class>
```

## Key
`{}`   specific range of occurrences


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Virtualization | Specifies whether virtualization is used when loading the class. | One of the following values: "enabled" , "disabled"| Yes |
| ProgId | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |
| VersionIndependentProgId | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| AutoConvertTo | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| InsertableObject | Indicates that this class is insertable. | Boolean.| Yes |
| ShortDisplayName | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | A string between 1 and 40 characters in length.| Yes |
| Id | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| DisplayName | A localizable string corresponding to the default value of the CLSID's key. | A string between 1 and 256 characters in length. This string is localizable.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [ImplementedCategories](element-com5-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com5-conversion.md) | Specifies the formats an application can read and write. |
| [DataFormats](element-com5-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [MiscStatus](element-com5-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com5-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com5-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com5-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [TypeLib](element-com5-typelib.md) | A type library for a class or interface.  |

## Requirements

| Item | Value |
| ---------------| -------------------------------------------------------------|
| com5 | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |
