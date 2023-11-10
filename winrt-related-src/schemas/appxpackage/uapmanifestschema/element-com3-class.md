---
title: com3:Class (in com3:ServiceServer)
description: Defines a ServiceServer class registration.
ms.date: 04/04/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:Class (in ServiceServer)

Defines a class registration in a COM server hosted in a Windows service that is registered in a [com3:ServiceServer](element-com3-serviceserver.md) element.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:Extension\>](element-com2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[com2:ComServer](element-com2-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[com3:ServiceServer](element-com3-serviceserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com3:Class\>**

## Syntax

```xml
<com3:Class
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    DisplayName = 'An optional string with a value between 1 and 256 characters in length.'
    EnableOleDefaultHandler = 'An optional boolean value.'
    ProgId = 'An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (e.g. Foo.Bar or Foo.Bar.1).'
    VersionIndependentProgId = 'An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (e.g. Foo.Bar or Foo.Bar.1).'
    AutoConvertTo = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    InsertableObject = 'An optional boolean value.'
    ShortDisplayName = 'An optional string with a value between 1 and 40 characters in length.' >

  <!-- Child elements -->
  ImplementedCategories?,
  Conversion?,
  DataFormats?,
  MiscStatus?,
  Verbs?,
  DefaultIcon?,
  ToolboxBitmap32? 
  
</com3:Class>
```

## Key

`?`    optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **EnableOleDefaultHandler** | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | An optional boolean value. | No |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (e.g. Foo.Bar or Foo.Bar.1). | No |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (e.g. Foo.Bar or Foo.Bar.1). | No |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** | Indicates that this class is insertable. | An optional boolean value. | No |  |
| **ShortDisplayName** | A short version of the class display name. | An optional string with a value between 1 and 40 characters in length. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [ImplementedCategories](element-com-exe-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com-exe-conversion.md) | Specifies the read/write permissions of a class. |
| [DataFormats](element-com-exe-dataformats.md) | Specifies the default and main data formats supported. |
| [MiscStatus](element-com-exe-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com-exe-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com-exe-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com-exe-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |

### Parent elements

| Parent element | Description |
|-|-|
| [com3:ServiceServer](element-com3-serviceserver.md) | Registers a COM server (with one or more class registrations) hosted in a Windows service that is declared with a corresponding [desktop6:Service](element-desktop6-service.md) element. |

## Examples

```xml
<?xml version="1.0" encoding="utf-8"?>
<Package IgnorableNamespaces="uap com com2 com3 desktop6"
         xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
         xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
         xmlns:desktop6="http://schemas.microsoft.com/appx/manifest/desktop/windows10/6"
         xmlns:com="http://schemas.microsoft.com/appx/manifest/com/windows10"
         xmlns:com2="http://schemas.microsoft.com/appx/manifest/com/windows10/2"
         xmlns:com3="http://schemas.microsoft.com/appx/manifest/com/windows10/3">
...
    <Applications>
        <Application ...>
            <Extensions>
                <desktop6:Extension Category="windows.service" Executable="ContosoPackagedService.exe" EntryPoint="packagedServiceComServer.service">
                    <desktop6:Service Name="examplePackagedServiceComServer" StartupType="manual" StartAccount="localService" /> 
                </desktop6:Extension>
                <com2:Extension Category="windows.comServer">
                    <com2:ComServer>
                        <com3:ServiceServer ServiceName="examplePackagedServiceComServer" DisplayName="ServicePackage public service server" 
                            LaunchAndActivationPermission="O:SYG:SYD:(A;;11;;;WD)(A;;11;;;RC)(A;;11;;;AC)(A;;11;;;AN)S:P(ML;;NX;;;S-1-16-0)">
                            <com3:Class Id="1BB09D24-6A0F-4C1F-BCB5-FB924324B2F5" DisplayName="CLSID_ContosoPublicServiceNoHandler"/>
                        </com3:ServiceServer>
                        <com3:TreatAsClass Id="2DAA3C97-F340-4C0E-B23C-92338974C5E9" DisplayName="CLSID_ContosoPublicServiceTreatAs" 
                            TreatAs="1BB09D24-6A0F-4C1F-BCB5-FB924324B2F5"/>
                        <com3:ProgId Id="ContosoPublicServiceNoHandler" Clsid="1BB09D24-6A0F-4C1F-BCB5-FB924324B2F5"/>
                        <com3:ProgId Id="ContosoPublicServiceNoHandler.1" CurrentVersion="ContosoPublicServiceNoHandler"/>
                    </com2:ComServer>
                </com2:Extension>
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |
