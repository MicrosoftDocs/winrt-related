---
title: com4:Class (in InProcessHandler)
description:  Defines an in-process handler class registration. (in com4:InProcessHandler)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in InProcessHandler)

Defines an in-process handler class registration.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessHandler\>](element-com4-inprocesshandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessHandler\>](element-com4-inprocesshandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
    Virtualization = 'A string that can have one of the following values: "enabled" or "disabled".'
    ProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    VersionIndependentProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    AutoConvertTo = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    InsertableObject = 'A boolean value.'
    ShortDisplayName = 'A string with a value between 1 and 40 characters in length.'
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' >

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

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
| -----------| -------------| -----------| ----------|-|
| **Virtualization** | Specifies whether virtualization is used when loading the class.  | A string that can have one of the following values: *enabled* or *disabled*. | Yes |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | No |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | No |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** | Indicates that this class is insertable. | A boolean value. | No |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | No |  |
| **Id** | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | The class display name. | A string with a value between 1 and 256 characters in length. This string is localizable. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [ImplementedCategories](element-com4-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com4-conversion.md) | Specifies the formats an application can read and write. |
| [DataFormats](element-com4-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [MiscStatus](element-com4-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com4-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com4-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com4-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [TypeLib](element-com4-class-typelib.md) | A type library for a class or interface. |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:InProcessHandler](element-com4-inprocesshandler.md) | Registers an in-process handler with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
