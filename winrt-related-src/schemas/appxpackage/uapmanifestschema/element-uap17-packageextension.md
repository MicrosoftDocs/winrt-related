---
title: uap17:PackageExtension
description: Declares an app extensibility point of type windows.packageExtension.
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:PackageExtension

Declares an app extensibility point of type windows.packageExtension.

## Description

Declares an app extensibility point of type *windows.packageExtension*. This element indicates which categories of extensions the package intends to consume and/or host.


## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-uap17-extension.md">&lt;uap17:Extension&gt;</a></dt>
<dd>
<b>&lt;uap17:PackageExtension&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap17:PackageExtension     Name = A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.
    Id = A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.
    PublicFolder? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    Description? = An optional string with a value between 1 and 2048 characters in length.
>
<!-- Child elements -->
  Properties{0,unbounded}
</uap17:PackageExtension>
```

## Key
`?`    optional (zero or one) 
`{}`   specific range of occurrences


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Name | The type of extension that the app intends to consume and/or host. | A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.| Yes |
| Id | The entry point by which the host app accesses the extension category instance, if there are multiple entry points. | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.| Yes |
| PublicFolder | The folder that the instance declares as the location where a host can have read access to files through a broker. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| No |
| DisplayName |  A friendly name for the app extension that can be displayed to users. | A string with a value between 1 and 256 characters in length. | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| Description | The description of the app. | An optional string with a value between 1 and 2048 characters in length.| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Properties](element-uap17-properties.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | http://schemas.microsoft.com/appx/manifest/uap/windows10/17 |
