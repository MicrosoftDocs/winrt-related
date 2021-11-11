---

title: desktop7:RuntimeExceptionHelperModule
description: Specifies a module that will be launched in the event of a runtime exception.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:RuntimeExceptionHelperModule

## Description
Specifies a module that will be launched in the event of a runtime exception.

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
<dt><a href="element-desktop7-desktopappmigration.md">&lt;desktop7:ErrorReporting&gt;</a></dt>
<dd><b>&lt;desktop7:RuntimeExceptionHelperModule&gt;</b></dd>
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
<desktop7:RuntimeExceptionHelperModule Path   = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.   >
</desktop7:RuntimeExceptionHelperModule>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The package-relative path to the module. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |


### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [ErrorReporting](element-desktop7-errorreporting.md) | Specifies a set of runtime exception helper modules. |  


## Remarks

The system will resolve this to an absolute path and write a value with this path as the value name to the **RuntimeExceptionHelperModules** subkey of the WER settings key for the specified scope (either machine or user scope is supported). At runtime this is used in the same way as a value written by an unpackaged app installer.


## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |