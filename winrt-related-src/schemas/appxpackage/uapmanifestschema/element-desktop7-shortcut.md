---

title: desktop7:Shortcut
description: Creates a shortcut to a file.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:Shortcut

## Description
Creates a shortcut to a file.

## Element Hierarchy
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
<dt><a href="element-desktop7-extension.md">&lt;desktop7:Extension&gt;</a></dt>
<dd><b>&lt;desktop7:Shortcut&gt;</b></dd>
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
```xml
<desktop7:Shortcut   File          =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                    Icon          =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                    Arguments?          =  A string between 1 and 256 characters in length. 
                    PinToStartMenu          =  Boolean
                    ExcludeFromShowInNewInstall   = Boolean
                    Description=  A string between 1 and 2048 characters in length.
                    desktop10:DisplayName? = A string between 1 and 256 characters in length. This string is localizable.
                    desktop10:Description? = A string between 1 and 2048 characters in length. This string is localizable.>
    desktop7:AppMigrations?
</desktop7:Shortcut>
```

### Key
`?` optional (zero or one) 

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| File | The path to the file that is the target of the shortcut. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |
| Icon | The path to the file that is the icon of the shortcut. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |
| Arguments | Arguments to the shortcut. | A string between 1 and 256 characters in length | No |
| PinToStartMenu | A boolean value specifying if the shortcut is pinned to the Start menu. | Boolean. | No |
| ExcludeFromShowInNewInstall  | A boolean value specifying if the shortcut should be excluded from the highlighting that is applied to newly installed apps. | Boolean.  | No |
| Description  | The description of the shortcut.  | A string between 1 and 256 characters in length.  | No |
| desktop10:DisplayName | The display name for the shortcut. | A string between 1 and 256 characters in length. This string is localizable. | No |
| desktop10:Description | The localizable description for the shortcut. | A string between 1 and 2048 characters in length. This string is localizable. | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop7:AppMigrations](element-desktop7-appmigrations.md) | Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app. |  


### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks




## Requirements

| Namespace |       Value                                                      |
|---------------|-------------------------------------------------------------|
| desktop7 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| desktop10 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |