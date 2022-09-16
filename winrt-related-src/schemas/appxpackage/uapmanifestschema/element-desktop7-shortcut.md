---
title: desktop7:Shortcut
description: Creates a shortcut to a file.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:Shortcut

Creates a shortcut to a file.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:Shortcut\>**

## Syntax

```xml
<desktop7:Shortcut
    File =  'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    Icon = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    Arguments = 'An optional string with a value between 1 and 256 characters in length.'
    PinToStartMenu = 'A boolean value.'
    ExcludeFromShowInNewInstall = 'A boolean value.'
    Description = 'A string with a value between 1 and 2048 characters in length.'
    desktop10:DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
    desktop10:Description = 'An optional string with a value between 1 and 2048 characters in length. This string is localizable.' >

    desktop7:AppMigrations?

</desktop7:Shortcut>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The path to the file that is the target of the shortcut. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **Icon** | The path to the file that is the icon of the shortcut. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **Arguments** | Arguments to the shortcut. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **PinToStartMenu** | A boolean value specifying if the shortcut is pinned to the Start menu. | A boolean value. | No |  |
| **ExcludeFromShowInNewInstall**  | A boolean value specifying if the shortcut should be excluded from the highlighting that is applied to newly installed apps. | A boolean value. | No |  |
| **Description**  | The description of the shortcut.  | A string with a value between 1 and 2048 characters in length.  | No |  |
| **desktop10:DisplayName** | The display name for the shortcut. | An optional string with a value between 1 and 256 characters in length. This string is localizable. | No |  |
| **desktop10:Description** | The localizable description for the shortcut. | An optional string with a value between 1 and 2048 characters in length. This string is localizable. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop7:AppMigrations](element-desktop7-appmigrations.md) | Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app. |  

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| desktop10 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
