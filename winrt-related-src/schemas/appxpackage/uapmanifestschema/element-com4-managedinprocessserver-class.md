---
title: com4:Class (in com4:ManagedInProcessServer)
description: Registers a managed in-process server with one or more classes. (in com4:ManagedInProcessServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in ManagedInProcessServer)

Registers a managed in-process server with one or more classes.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:ManagedInProcessServer\>](element-com4-managedinprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
  ThreadingModel = 'A string that can have one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
  ImplementationClass = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  Virtualization = 'A string that can have one of the following values: "enabled" or "disabled".'
  ProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  VersionIndependentProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  AutoConvertTo = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  InsertableObject = 'A boolean value.'
  ShortDisplayName = 'A string with a value between 1 and 40 characters in length.'
  Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ThreadingModel** | The threading model for loading DLLs. | A string that can have one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, or *Neutral*. | Yes |  |
| **ImplementationClass** | The implementation class associated with the class reference. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **Virtualization** | Specifies whether virtualization is used when loading the class. | A string that can have one of the following values: *enabled* or *disabled*. | Yes |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **InsertableObject** | Indicates that this class is insertable. | A boolean value. | Yes |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | Yes |  |
| **Id** | The Id attribute corresponds to the CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:ManagedInProcessServer](element-com4-managedinprocessserver.md) | Registers a managed in-process server with one or many class registrations. |

## Examples

The following example shows the registration of multiple class implementations with a managed in-process server.

```xml
<com4:ManagedInProcessServer Assembly="Fabrikam.Widgets, Version=10.0.0.0, Culture=neutral, PublicKeyToken=xxxxxxxxxxxxxxxxx" RuntimeVersion="v4.0.30319"> 
  <com4:Class Id="99b9b8fa-2c14-42f7-xxxx-xxxxxxxxxxxx" DisplayName="SimpleWidget" ImplementationClass="Fabrikam.Widgets.SimpleWidget"/> 
  <com4:Class Id="0057c8be-3c95-4242-xxxx-xxxxxxxxxxxx" DisplayName="SingleThreadedWidget" ImplementationClass="Fabrikam.Widgets.SingleThreadedWidget" ThreadingModel="Apartment"/> 
</com4:ManagedInProcessServer> 
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
