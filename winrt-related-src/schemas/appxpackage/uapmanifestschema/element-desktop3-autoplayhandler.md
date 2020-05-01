---

title: desktop3:AutoPlayHandler
description: Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:AutoPlayHandler

## Description
Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC.

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
<dt><a href="element-desktop3-extension.md">&lt;desktop3:Extension&gt;</a></dt>
<dd><b>&lt;desktop3:AutoPlayHandler&gt;</b></dd>
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
```syntax
<desktop3:AutoPlayHandler>
    desktop3:InvokeAction{0,1000}
</desktop3:AutoPlayHandler>
```

### Key
`{}` specific range of occurrences


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop3:InvokeAction](element-desktop3-invokeaction.md) | Contains content and device information for invoking an AutoPlay action. |  

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |