---

title: uap5:ExecutionAlias
description: The executable of a UWP app to be activated from a command prompt.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:ExecutionAlias
The executable of a UWP app to be activated from a command prompt.

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
<dt><a href="element-uap5-appexecutionalias.md">&lt;uap5:AppExecutionAlias&gt;</a></dt>
<dd><b>&lt;uap5:ExecutionAlias&gt;</b></dd>
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
<uap5:ExecutionAlias Alias = An executable in the form of a string followed by ".exe". />
```

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Alias | The name of the UWP app executable. | An executable in the form of a string followed by ".exe". | Yes |
| uap8:AllowOverride | A value that indicates whether to override the UWP app executable. | Boolean value. | No |


## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5`</br></br>`http://schemas.microsoft.com/appx/manifest/uap/windows10/8` (for the **uap8:AllowOverride** attribute) |
