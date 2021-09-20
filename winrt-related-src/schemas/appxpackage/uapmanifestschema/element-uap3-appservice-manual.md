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


Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app, or for a background task invoked to service an app contract a way to communicate with its caller.

## Element hierarchy

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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd><b>&lt;uap3:AppService&gt;</b></dd>
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


```
<uap3:AppService Name                            = A string between 2 and 39 characters in length 
                                                   that consists of alphanumeric, period (except 
                                                   for the first character), and dash characters 
                                                   only.
                 ServerName?                     = An alphanumeric string between 1 and 255 
                                                   characters in length. Must begin with an 
                                                   alphabetic character.
                 SupportsRemoteSystems?          = boolean 
                 uap4:SupportsMultipleInstances? = boolean >
</uap3:AppService>
```

**Key**

          ? optional (zero or one)

## Attributes and Elements


**Attributes**

| Attribute | Description | Data type  | Required | Default value |
|-----------|-------------|------------|----------|---------------|
| **Name**  | The service name (used to match the caller of the Application Contract with the provider). | A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes  |
| **ServerName**  | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No   |  |
| **SupportsRemoteSystems** | Indicates whether or not to allow access to the endpoint for the app service from a remote endpoint.| boolean  | No  |    |
| **uap4:SupportsMultipleInstances** | Supports multiple, separate instances of app services. | boolean  | No  |    |


 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                 | Description                                  |
|------------------------------------------------|----------------------------------------------|
| [**uap:Extension**](element-uap-extension.md) | Declares an extensibility point for the app. |


## Remarks
Note that to use the uap3 or uap4 schema elements, you must have the correct version of Windows 10 and include the associated XML schema namespace. For more information about schema versions, see [What's different in Windows 10](what-s-changed-in-windows-10.md).  

## Examples


```XML
<Package ...
         xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"  
         ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="uap uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap:Extension Category="windows.appService" 
                               Executable="App1.exe" 
                               EntryPoint="FabrikamService.InventoryServiceTask">    
                    <uap3:AppService Name="com.fabrikam.inventoryService" 
                                     SupportsRemoteSystems="true"/>  
                </uap:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |

 

 

 



