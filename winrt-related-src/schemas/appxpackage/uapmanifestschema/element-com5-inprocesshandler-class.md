---
title: com5:Class (in InProcessHandler)
description: Defines an in-process handler class registration. (in com5:InProcessHandler)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com5:Extension, com5:ComServer, com5:InProcessHandler, com5:Class]
---

# com5:Class (in InProcessHandler)

Defines an in-process handler class registration.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Class>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Class>`**

## Syntax

```xml
<com5:Class
  Virtualization = 'An optional string that can have one of the following values: "enabled", or "disabled".'
  ProgId = 'An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1'
  VersionIndependentProgId = 'An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1'
  AutoConvertTo = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  InsertableObject = 'An optional boolean value.'
  ShortDisplayName = 'An optional string between 1 and 40 characters in length.'
  Id = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  com5:ImplementedCategories?
  com5:Conversion?
  com5:DataFormats?
  com5:MiscStatus?
  com5:Verbs?
  com5:DefaultIcon?
  com5:ToolboxBitmap32?
  com5:TypeLib?

</com5:Class>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Virtualization** |  Specifies whether virtualization is used when loading the class.  | An optional string that can have one of the following values: *enabled*, *disabled*. | No |  |
| **ProgId** |  Associates a programmatic identifier (ProgID) with a CLSID.  | An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |  |
| **VersionIndependentProgId** |  Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application.  | An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |  |
| **AutoConvertTo** |  Specifies the automatic conversion of a given class of objects to a new class of objects.  | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** |  Indicates that this class is insertable.  | An optional boolean value. | No |  |
| **ShortDisplayName** |  A short version of the class display name.  | An optional string between 1 and 40 characters in length. | No |  |
| **Id** |  The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}).  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** |  A localizable string corresponding to the default value of the CLSID's key.  | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com5:ImplementedCategories](element-com5-implementedcategories.md) | Specifies categories implemented by the class. |
| [com5:Conversion](element-com5-conversion.md) | Specifies the formats an application can read and write. |
| [com5:DataFormats](element-com5-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [com5:MiscStatus](element-com5-miscstatus.md) | Specifies how to create and display an object. (com5:MiscStatus) |
| [com5:Verbs](element-com5-verbs.md) | Specifies the verbs to be registered for an application. |
| [com5:DefaultIcon](element-com5-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [com5:ToolboxBitmap32](element-com5-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [com5:TypeLib](element-com5-typelib.md) | A type library for an interface |

## Parent elements

| Parent element | Description |
|-|-|
| [com4:InProcessHandler](element-com4-inprocesshandler.md) | Registers an in-process handler with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
