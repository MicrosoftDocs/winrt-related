---
title: desktop7:ErrorReporting
description: Specifies a set of runtime exception helper modules.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ErrorReporting

Specifies a set of runtime exception helper modules.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:ErrorReporting\>**

## Syntax

```xml
<desktop7:ErrorReporting>

    desktop7:RuntimeExceptionHelperModule{0,10000}

</desktop7:ErrorReporting>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop7:RuntimeExceptionHelperModule](element-desktop7-runtimeexceptionhelpermodule.md) | Specifies a module that will be launched in the event of a runtime exception. |  

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Remarks

This extension enables packaged applications to hook into Windows Error Reporting analysis as documented in [WerRegisterRuntimeExceptionModule function](/windows/win32/api/werapi/nf-werapi-werregisterruntimeexceptionmodule) and [WER Settings](/windows/win32/wer/wer-settings). To use this extension the package must have the ability to implement in-process extensions, for instance using an external location.
To use this extension the package must have the ability to implement in-process extensions, for instance using an external location.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
