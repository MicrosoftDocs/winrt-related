---
title: com4:Class (in ManagedInProcessServer)
description: Registers a managed in-process server with one or more classes. (in com4:ManagedInProcessServer)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com4:ManagedInProcessServer, com4:Class]
---

# com4:Class (in ManagedInProcessServer)

Registers a managed in-process server with one or more classes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ManagedInProcessServer>`](element-com4-managedinprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Class>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ManagedInProcessServer>`](element-com4-managedinprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Class>`**

## Syntax

```xml
<com4:Class
  ThreadingModel = 'An optional string that can have one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
  ImplementationClass = 'A required alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1'
  Virtualization = 'An optional string that can have one of the following values: "enabled", or "disabled".'
  ProgId = 'An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1'
  VersionIndependentProgId = 'An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1'
  AutoConvertTo = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  InsertableObject = 'An optional boolean value.'
  ShortDisplayName = 'An optional string between 1 and 40 characters in length.'
  Id = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  com4:ImplementedCategories?
  com4:Conversion?
  com4:DataFormats?
  com4:MiscStatus?
  com4:Verbs?
  com4:DefaultIcon?
  com4:ToolboxBitmap32?
  com4:TypeLib?

</com4:Class>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ThreadingModel** | The threading model for loading DLLs. | An optional string that can have one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, *Neutral*. | No |  |
| **ImplementationClass** | The implementation class associated with the class reference. | A alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | Yes |  |
| **Virtualization** | Specifies whether virtualization is used when loading the class. | An optional string that can have one of the following values: *enabled*, *disabled*. | No |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An optional alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** | Indicates that this class is insertable. | An optional boolean value. | No |  |
| **ShortDisplayName** | A short version of the class display name. | An optional string between 1 and 40 characters in length. | No |  |
| **Id** | The Id attribute corresponds to the CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:ImplementedCategories](element-com4-implementedcategories.md) | Specifies categories implemented by the class. |
| [com4:Conversion](element-com4-conversion.md) | Specifies the formats an application can read and write. |
| [com4:DataFormats](element-com4-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [com4:MiscStatus](element-com4-miscstatus.md) | Specifies how to create and display an object. |
| [com4:Verbs](element-com4-verbs.md) | Specifies the verbs to be registered for an application. |
| [com4:DefaultIcon](element-com4-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [com4:ToolboxBitmap32](element-com4-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [com4:TypeLib](element-com4-class-typelib.md) | Associates a type library with a class or interface. |

## Parent elements

| Parent element | Description |
|-|-|
| [com4:ManagedInProcessServer](element-com4-managedinprocessserver.md) | Registers a managed in-process server with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

<!-- Author content goes here -->

## Examples

The following example shows the registration of multiple class implementations with a managed in-process server.

```xml
<com4:ManagedInProcessServer Assembly="Fabrikam.Widgets, Version=10.0.0.0, Culture=neutral, PublicKeyToken=xxxxxxxxxxxxxxxxx" RuntimeVersion="v4.0.30319"> 
  <com4:Class Id="99b9b8fa-2c14-42f7-xxxx-xxxxxxxxxxxx" DisplayName="SimpleWidget" ImplementationClass="Fabrikam.Widgets.SimpleWidget"/> 
  <com4:Class Id="0057c8be-3c95-4242-xxxx-xxxxxxxxxxxx" DisplayName="SingleThreadedWidget" ImplementationClass="Fabrikam.Widgets.SingleThreadedWidget" ThreadingModel="Apartment"/> 
</com4:ManagedInProcessServer> 
```
