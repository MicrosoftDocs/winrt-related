---
description: Declares an extensibility point for the app (uap3:Extension).
Search.Product: eADQiWindows 10XVcnh
title: uap3:Extension (Windows 10)
ms.assetid: ed8f9296-0771-48ab-aecf-cca642e830c1


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Extension (Windows 10)

Declares an extensibility point for the app.

[ <  Package  > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< UAP3:Extension >**

## Syntax


```
<uap3:Extension Category       = "windows.appointmentDataProvider" | 
                                 "windows.emailDataProvider" | 
                                 "windows.contactDataProvider" | 
                                 "windows.appUriHandler" | 
                                 "windows.appExtensionHost" | 
                                 "windows.appExtension" |
                                 "windows.protocol" |
                                 "windows.fileTypeAssociation" |
                Executable?    = A string between 1 and 256 characters in length that must 
                                 end with ".exe" and cannot contain these characters: <, >, 
                                 :, ", |, ?, or *. It specifies the default executable for 
                                 the extension. If not specified, the executable defined 
                                 for the app is used.  If specified, the EntryPoint 
                                 property is also used. If that EntryPoint property isn&#39;t 
                                 specified, the EntryPoint defined for the app is used.
                EntryPoint?    = A string between 1 and 256 characters in length, 
                                 representing the  task handling the extension. This is 
                                 normally the fully namespace-qualified name of a 
                                 Windows Runtime type. If EntryPoint is not specified, 
                                 the EntryPoint defined for the app is used instead.
                RuntimeType?   = A string between 1 and 255 characters in length that 
                                 cannot start or end with a period or contain these 
                                 characters: <, >, :, ", /, \, |, ?, or *.
                StartPage?     = A string between 1 and 256 characters in length that 
                                 cannot contain these characters: <, >, :, ", |, ?, or *.
                ResourceGroup? = An alphanumeric string between 1 and 255 characters in 
                                 length. Must begin with an alphabetic character. .
                uap10:TrustLevel?       = String value. Can be one of the following: "appContainer", "mediumIL".
                uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
                uap10:HostId?           = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                uap10:Parameters?       = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
  <!-- Child elements -->
  ( uap3:appointmentDataProvider
  | uap3:emailDataProvider
  | uap3:contactDataProvider
  | uap3:appUriHandler
  | uap3:appService
  | uap3:appExecutionAlias
  | uap3:fileTypeAssociations
  )?

</uap3:Extension>
```

**Key**

          ? optional (zero or one)

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following: "windows.appExtensionHost", "windows.appExtension", "windows.appUriHandler", "windows.appointmentDataProvider", "windows.emailDataProvider", "windows.contactDataProvider", "windows.appExecutionAlias", "windows.appService", "windows.protocol", "windows.fileTypeAssociations" | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| ResourceGroup | The logical container where resources are managed. | An alphanumeric string between 1 and 255 characters in length. | No |
| uap10:TrustLevel | Specifies the trust level of the extension. | String value. Can be one of the following: "appContainer", "mediumIL".  | No |
| uap10:RuntimeBehavior | Specifies the run time behavior of the extension. | String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".  | No |
| uap10:HostId | Specifies the app ID of the host app for the extension. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.  | No |
| uap10:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.  | No |
| previewappcompat:CompatMode | Specifies the compatibility mode when viewing application previews. | A string value that can be one of the following: "classic", "modern". | No |
| previewappcompat:Scope | Contains paraeters to manipulate the scope used for application previews. | A string value that can be one of the following: "user", "machine". | No |
| uap11:Id | The unique identifier for the extensibility point. | A string between 1 and 256 characters in length. | No |
| uap11:Subsystem | Specifies the type of system the application will run on. | String value. Can be one of the following: "console", "windows". | No |
| uap11:SupportsMultipleInstances | Specifies whether or not the application supports multiple instances. | Boolean value. | No
| uap11:Resource Group | The logical container where resources are managed. | An alphanumeric string between 1 and 255 characters in length. | No |
| uap11:CurrentDirectoryPath | Specifies the current directory the of the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| uap11:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.  | No |
| desktop7:CompatMode | Specifies the compatibility mode when viewing application previews. | A string value that can be one of the following: "classic", "modern". | No |
| desktop7:Scope | Contains paraeters to manipulate the scope used for application previews. | A string value that can be one of the following: "user", "machine". | No |


**Child Elements**

| Child Element                                                                       | Description                                                                      |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**uap3:AppointmentDataProvider**](element-uap3-appointmentdataprovider-manual.md) | Declares an app extensibility point of type **windows.appointmentDataProvider**. |
| [**uap3:EmailDataProvider**](element-uap3-emaildataprovider-manual.md)             | Declares an app extensibility point of type **windows.emailDataProvider**.       |
| [**uap3:ContactDataProvider**](element-uap3-contactdataprovider-manual.md)         | Declares an app extensibility point of type **windows.contactDataProvider**.     |
| [**uap3:AppUriHandler**](element-uap3-appurihandler-manual.md)                     | Declares an app extensibility point of type **windows.appUriHandler**.           |
| [**uap3:AppExtensionHost**](element-uap3-appextensionhost-manual.md)               | Declares an app extensibility point of type **windows.appExtensionHost**.        |
| [**uap3:AppExtension**](element-uap3-appextension-manual.md)                       | Declares an app extensibility point of type **windows.appExtension**.            |
| [**uap3:AppService**](element-uap3-appservice-manual.md)                           | Declares an app extensibility point of type **windows.appExtension**.            |
| [**uap3:AppExeuctionAlias**](element-uap3-appexecutionalias.md)                    | Declares an app extensibility point of type **windows.appExecutionAlias**.       |
| [**uap3:Protocol**](element-uap3-protocol.md)                                      | Declares an app extensibility point of type **windows.protocol**.                |
| [**uap3:FileTypeAssociations**](element-uap3-filetypeassociations.md)              | Declares an app extensibility point of type **windows.fileTypeAssociationss**.   |

 

**Parent Elements**

| Parent Element                                                               | Description                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------|
| [**Extensions (type: CT_ApplicationExtensions)**](element-1-extensions.md) | Defines one or more extensibility points for the app. |

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appointmentDataProvider" 
                                EntryPoint="UserDataProvider.AppointmentDataProviderTask">  
                    <uap3:AppointmentDataProvider ServerName="MyDataProvider.PPLE" />  
                </uap3:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **uap3** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` | 
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **previewappcompat** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/msixappcompatsupport/3` |
| **UAP11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Desktop7** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |