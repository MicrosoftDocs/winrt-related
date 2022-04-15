---
description: Declares an app extensibility point of the type windows.webAccountProvider.
title: uap2:WebAccountProvider

keywords: windows 10, uwp, schema, package, manifest
ms.topic: reference
ms.date: 03/28/2022

---

# uap2:WebAccountProvider

Declares an app extensibility point of the type windows.webAccountProvider.

## Element Hierarchy

[ < Package > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Extensions > ](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP2:Extension > ](element-uap2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< UAP2:WebAccountProvider >**

## Syntax

```syntax 
<uap2:WebAccountProvider  Url                       = A string between 1 and 32767 characters in length in the form of a valid web url.
                          BackgroundEntryPoint      = A string between 1 and 256 characters in length, representing if EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                          DisplayName               =  A string between 1 and 256 characters in length.
                          DisplayPurpose            = A string between 1 and 2048 characters in length.
                          Square44x44Logo           = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters.
                          >

<!-- Child Elements -->
( uap2:managedUrls? )
</uap2:webAccountProvider>

```

## Attributes

| Attribute | Description | Data Type | Required |
|-----------|-------------|-----------|----------|
| Url | Specifies a URL to which a plugin may send cookies. | A string between 1 and 32767 characters in length in the form of a valid web url. | Yes |
| BackgroundEntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. | Yes |
| DisplayName | A friendly name that can be displayed to users | A string between 1 and 256 characters in length. This string is localizable. | No |
| DisplayPurpose | Represents the purpose for the account provider. | A string between 1 and 2048 characters in length. | No |
| Square44x44Logo | A path to a file that contains an image | A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", &#124;, ?, or *. In this string, the / and \ characters can't be the first or last characters. | No

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

## Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [uap2:Extension](element-uap2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Manifest Path |
|-----------|---------------|
| **UAP2** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2`