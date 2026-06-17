---
title: uap3:AppService
description: Declares an app extensibility point of type windows.appService (uap3:AppService).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppService]
---

# uap3:AppService

Declares an app extensibility point of type *windows.appService*. Application Contracts are a way for an app to invoke a background task belonging to another app, or for a background task invoked to service an app contract a way to communicate with its caller.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:AppService>`**  

## Syntax

```xml
<uap3:AppService
  SupportsRemoteSystems = 'An optional boolean value.'
  Name = 'A required string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  ServerName = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap4:SupportsMultipleInstances = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **SupportsRemoteSystems** | Indicates whether or not to allow access to the endpoint for the app service from a remote endpoint. | An optional boolean value. | No |  |
| **Name** | The service name (used to match the caller of the Application Contract with the provider). | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **ServerName** | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap4:SupportsMultipleInstances** | Supports multiple, separate instances of app services. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **uap4** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

> [!NOTE]
> To use the uap3 or uap4 schema elements, you must have the correct version of Windows 10 and include the associated XML schema namespace. For more information about schema versions, see [What's different in Windows 10](what-s-changed-in-windows-10.md).

## Examples

```xml
<Package
    xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"  
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap:Extension
                    Category="windows.appService" 
                    Executable="App1.exe" 
                    EntryPoint="FabrikamService.InventoryServiceTask">    
                    <uap3:AppService
                        Name="com.fabrikam.inventoryService" 
                        SupportsRemoteSystems="true"/>  
                </uap:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```
