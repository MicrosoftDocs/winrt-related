---
title: desktop7:ErrorReporting
description: Specifies a set of runtime exception helper modules.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ErrorReporting

## Description
Specifies a set of runtime exception helper modules.

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
<dd><b>&lt;desktop7:ErrorReporting&gt;</b></dd>
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
<desktop7:ErrorReporting>
    desktop7:RuntimeExceptionHelperModule{0,10000}
</desktop7:ErrorReporting>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop7:RuntimeExceptionHelperModule](element-desktop7-runtimeexceptionhelpermodule.md) | Specifies a module that will be launched in the event of a runtime exception. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks

This extension enables packaged applications to hook into Windows Error Reporting analysis as documented in [WerRegisterRuntimeExceptionModule function](/windows/win32/api/werapi/nf-werapi-werregisterruntimeexceptionmodule) and [WER Settings](/windows/win32/wer/wer-settings). To use this extension the package must have the ability to implement in-process extensions, for instance using an external location.
To use this extension the package must have the ability to implement in-process extensions, for instance using an external location.

## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |