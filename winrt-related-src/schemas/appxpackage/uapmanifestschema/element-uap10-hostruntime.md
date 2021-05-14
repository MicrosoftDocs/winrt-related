---

title: uap10:HostRuntime
description: This extension provides a means to deliver translated app resources.
ms.date: 03/05/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:HostRuntime

## Description
Defines a package-wide extension that defines the runtime information to be used when activating a [hosted app](/windows/uwp/launch-resume/hosted-app-packages).

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-extension.md">&lt;uap10:Extension&gt;</a></dt>
<dd><b>&lt;uap10:HostRuntime&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap10:HostRuntime Id =  An ASCII string between 1 and 256 characters in length. />
```

### Key
`?`   optional (zero or one)

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id |  The unique identifier of this specific host app in the package. | Yes |

### Child Elements
None

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |