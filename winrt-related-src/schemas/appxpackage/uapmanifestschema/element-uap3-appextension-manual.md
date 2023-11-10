---
description: Declares an app extensibility point of type windows.appExtension.
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppExtension
ms.assetid: 88e4b56d-e2c2-4782-bedd-eae33d069c2c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:AppExtension

Declares an app extensibility point of type *windows.appExtension*. This element indicates which categories of extensions the app intends to consume and/or host.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:AppExtension\>**

## Syntax

```xml
<uap3:AppExtension
    Name = 'A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
    Id = 'A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
    PublicFolder = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    DisplayName = 'A string with a value between 1 and 256 characters in length.'
    Description = 'A string between 1 and 2048 characters in length.' >

  <!-- Child elements -->
  uap3:Properties?

</uap3:AppExtension>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Description** | The description of the app | A string between 1 and 2048 characters in length. | No |  |
| **DisplayName**  | A friendly name for the app extension that can be displayed to users. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **Id** | The entry point by which the host app accesses the extension category instance, if there are multiple entry points. | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **Name** | The type of extension that the app intends to consume and/or host. | A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **PublicFolder** | The folder that the instance declares as the location where a host can have read access to files through a broker. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [uap3:Properties](element-uap3-properties-manual.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app. |

## Examples

The following example indicates that the app hosts or consumes the low-performance browser extension

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension 
                    Category="windows.appExtension">  
                    <uap3:AppExtension
                        Name="com.microsoft.browser.ext"
                        Id="Extension.Low.Performance"
                        PublicFolder="public\lowperf"
                        DisplayName="Low Performance Extension"/>  
                </uap3:Extension>  
              </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
