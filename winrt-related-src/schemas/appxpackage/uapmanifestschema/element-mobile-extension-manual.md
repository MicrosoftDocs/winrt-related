---
description: Declares an extensibility point for the app (mobile:Extension).
Search.Product: eADQiWindows 10XVcnh
title: mobile:Extension (Windows 10)
ms.assetid: 0f9f4bee-3a63-4383-86db-a555ca4ccad6
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:Extension (Windows 10)

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<mobile:Extension\>](element-mobile-extension-manual.md)

## Syntax

```xml
<mobile:Extension
    Category = 'A string that can have one of the following values: "windows.aowApp", "windows.mobileMultiScreenProperties", "windows.communicationBlockingProvider", or "windows.phoneCallOriginProvider".'
    Executable = 'An optional string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used.'
    EntryPoint = 'An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
    RuntimeType = 'An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
    ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
    StartPage = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' >

  <!-- Child elements -->
  mobile:AowApp
  mobile:MobileMultiScreenProperties?

</mobile:Extension>
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of app extensibility point. | A string that can have one of the following values: *windows.aowApp*, *windows.mobileMultiScreenProperties*, *windows.communicationBlockingProvider*, or *windows.phoneCallOriginProvider*. | Yes |  |
| **Executable** | The default launch executable. | An optional string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **RuntimeType** | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md). | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [mobile:AowApp](element-mobile-aowapp-manual.md) | Declares an app extensibility point of type **windows.aowApp**. |
| [mobile:MobileMultiScreenProperties](element-mobile-mobilemultiscreenproperties-manual.md) | Declares an app extensibility point of type **windows.MobileMultiScreenProperties**. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Examples

The following example shows how to block your mobile app from being displayed on a connected display. This markup will cause your app's tile to be disabled on the connected display’s Start menu.

```xml
<Package
    xmlns:mobile="http://schemas.microsoft.com/appx/manifest/mobile/windows10"
    IgnorableNamespaces="... mobile">
    <Applications>
        <Application>
            <Extensions>
                <mobile:Extension
                    Category="windows.mobileMultiScreenProperties">
                    <mobile:MobileMultiScreenProperties
                        RestrictToInternalScreen="true"/>
                </mobile:Extension>
            </Extensions>
        </Application>
    </Applications>
</Package>      
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/mobile/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
