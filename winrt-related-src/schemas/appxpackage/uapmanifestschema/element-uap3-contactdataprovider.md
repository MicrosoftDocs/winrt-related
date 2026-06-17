---
title: uap3:ContactDataProvider
description: Declares an app extensibility point of type windows.contactDataProvider.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:ContactDataProvider]
---

# uap3:ContactDataProvider

Declares an app extensibility point of type *windows.contactDataProvider*.

This element enables apps to become data providers for contacts. A data provider is an application that can fully replace the built-in synchronization engine for the contacts as the synchronization engine for an account. A data provider can not only synchronize the data associated with the account, but can also provide implementations for secondary APIs, such as those required to compose Secure/Multipurpose Internet Mail Extensions (S/MIME) messages or perform server searches on behalf of another application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:ContactDataProvider>`**  

## Syntax

```xml
<uap3:ContactDataProvider
  ServerName = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServerName** | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.contactDataProvider" 
                    EntryPoint="UserDataProvider.ContactDataProviderTask" />  
            </Extensions>
        </Application>
    </Applications>
</Package>
```
