---
title: desktop7:AppMigrations
description: Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:AppMigrations

## Description
Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app.

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
<dd><b>&lt;desktop7:AppMigrations&gt;</b></dd>
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
<desktop7:AppMigrations>
    desktop7:AppMigration{0,1000}
</desktop7:AppMigrations>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop7:AppMigration](element-desktop7-appmigration.md) | Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Shortcut](element-desktop7-shortcut.md) | Creates a shortcut to a file. |  


## Remarks



## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |