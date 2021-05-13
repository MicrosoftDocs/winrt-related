---

title: uap5:Instancing
description: Specifies whether the executable runs as a single instance or can run as multiple instances.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:Instancing

## Description
Specifies whether the executable runs as a single instance or can run as multiple instances.

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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-outofprocessserver.md">&lt;uap5:OutOfProcessServer&gt;</a></dt>
<dd><b>&lt;uap5:Instancing&gt;</b></dd>
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
```syntax
<uap5:Instancing>
  "singleInstance" | "multipleInstances"
</uap5:Instancing>
```

## Attributes and Elements
### Attributes
None

### Child Elements
None

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |

