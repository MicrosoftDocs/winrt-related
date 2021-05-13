---

title: uap5:StartupTask
description: Specifies a startup task for your application.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:StartupTask

## Description
Specifies a startup task for your application. 

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
<dd><b>&lt;uap5:StartupTask&gt;</b></dd>
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
<uap5:StartupTask TaskId       = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                  Enabled?     = Boolean.
                  DisplayName? = A string between 1 and 256 characters in length. This string is localizable. />
```

### Key


## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| TaskId | A unique identifier for your task. Using this identifier, your app can call the APIs in the Windows.ApplicationModel.StartupTask class to programmatically enable or disable a startup task. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Enabled | Indicates whether the task first starts enabled or disabled. Enabled tasks will run the next time the user logs on (unless it has been disabled by the user). | Boolean. | No |
| DisplayName | The name of the task that appears in the Task Manager. This string is localizable using ms-resource. | A string between 1 and 256 characters in length. This string is localizable. | No |


## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
