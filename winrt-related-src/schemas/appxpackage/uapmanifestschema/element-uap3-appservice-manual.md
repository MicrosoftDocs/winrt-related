---
description: Declares an app extensibility point of type windows.appService (uap3:AppService).
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppService
ms.assetid: 1a5170ca-cd60-4102-a451-b4d9ad81a6e7
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:AppService

Declares an app extensibility point of type *windows.appService*. Application Contracts are a way for an app to invoke a background task belonging to another app, or for a background task invoked to service an app contract a way to communicate with its caller.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:AppService\>**

## Syntax

```xml
<uap3:AppService
    Name = 'A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes.'
    ServerName = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
    SupportsRemoteSystems = 'An optional boolean value.' 
    uap4:SupportsMultipleInstances = 'An optional boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type  | Required | Default value |
|-|-|-|-|-|
| **Name** | The service name (used to match the caller of the Application Contract with the provider). | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes. | Yes |  |
| **ServerName** | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **SupportsRemoteSystems** | Indicates whether or not to allow access to the endpoint for the app service from a remote endpoint.| An optional boolean value. | No |  |
| **uap4:SupportsMultipleInstances** | Supports multiple, separate instances of app services. | An optional boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
