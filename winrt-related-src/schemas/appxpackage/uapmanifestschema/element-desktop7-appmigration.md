---

title: desktop7:AppMigration
description: Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:AppMigration

## Description
Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app.

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
<dd>
<dl>
<dt><a href="element-desktop7-shortcut.md">&lt;desktop7:Shortcut&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-appmigrations.md">&lt;desktop7:AppMigrations&gt;</a></dt>
<dd><b>&lt;desktop7:AppMigration&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
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
<desktop7:AppMigration Executable   = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. 
                        AumId   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
</desktop7:AppMigration>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Executable | The executable to which shortcuts should be migrated. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", \|, ?, or *. | No |
| AumId | The Application User Model ID of the Desktop app for which shortcuts should be migrated from. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [AppMigrations](element-desktop7-appmigrations.md) | Specifies a set of app migration entries for a shortcut. |  


## Remarks



## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |