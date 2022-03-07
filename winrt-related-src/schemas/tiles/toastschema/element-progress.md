---
description: Specifies a progress bar for a toast notifcation. Only supported on toasts on Desktop, build 15063 or later.
Search.Product: eADQiWindows 10XVcnh
title: progress
keywords: windows 10, uwp, schema, toast notifications
ms.topic: reference
ms.date: 03/01/2022
---

# progress  (Toast XML Schema)

Specifies a progress bar for a toast notification. Only supported on toasts on Desktop, build 15063 or later.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-binding.md">&lt;binding&gt;</a></dt>
<dd><b>&lt;progress&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax

``` syntax
<progress title? = string
    status = string
    value = string
    valueStringOverride? = string
/>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

| Attribute | Description | Data type | Required | Default value |
|-----------|-------------|-----------|----------|---------------|
| title   | An optional title string.  | string    | No      | None          |
| status      | A status string that is displayed underneath the progress bar on the left. This string should reflect the status of the operation, like "Downloading..." or "Installing..."  | string   | Yes      | None          |
| value | The value of the progress bar. This value either be a floating point number between 0.0 and 1.0 or the value "indeterminate", which results in a loading animation | string | Yes | 0 |
| valueStringOverride | An optional string to be displayed instead of the default percentage string. If this isn't provided, something like "70%" will be displayed. | string | No | None |


### Child Elements

None

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [binding](element-binding.md) | Specifies the toast template. Note that only one binding element can be included in a toast notification. |

## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
