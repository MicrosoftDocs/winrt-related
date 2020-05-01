---

description: A type representing an HRESULT error code.
title: winrt::hresult_error struct (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/25/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, hresult, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::hresult_error struct (C++/WinRT)
A type representing an HRESULT error code.

## Syntax
```cppwinrt
struct hresult_error
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[hresult_error::hresult_error constructor](#hresult_errorhresult_error-constructor)|Initializes a new instance of the **hresult_error** struct with a copy of the input data.|

## Types
|Constructor|Description|
|------------|-----------------|
|[hresult_error::from_abi_t type](#hresult_errorfrom_abi_t-type)|The type of the [hresult_error::from_abi](#hresult_errorfrom_abi_t-type) static data member.|

## Static data members
|Function|Description|
|------------|-----------------|
|[hresult_error::from_abi static data member](#hresult_errorfrom_abi-static-data-member)|An instance of type [hresult_error::from_abi_t](#hresult_errorfrom_abi_t-type), which can be passed to the constructor of **hresult_error** (or a derived type) to indicate that the constructor should try to retrieve restricted error info.|

## Member functions
|Function|Description|
|------------|-----------------|
|[hresult_error::code function](#hresult_errorcode-function)|Retrieves the code for the error represented by the **hresult_error** object.|
|[hresult_error::message function](#hresult_errormessage-function)|Retrieves the message for the error represented by the **hresult_error** object.|
|[hresult_error::to_abi function](#hresult_errorto_abi-function)|Sets the restricted error information object for the current thread, and returns the code for the error represented by the **hresult_error** object.|
|[hresult_error::try_as function](#hresult_errortry_as-function)|Returns the requested interface, if it is supported. Returns `nullptr`, or `false`, if it is not.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[hresult_error::operator= (assignment operator)](#hresult_erroroperator-assignment-operator)|Assigns a value to the **hresult_error** object.|

## hresult_error::hresult_error constructor
Initializes a new instance of the **hresult_error** struct with a copy of the input data.

### Syntax
```cppwinrt
hresult_error() noexcept;
hresult_error(hresult_error&&);
hresult_error(hresult_error const& other);
explicit hresult_error(HRESULT const code) noexcept;
hresult_error(HRESULT const code, winrt::hstring const& message, ::IUnknown* object = nullptr) noexcept;
hresult_error(HRESULT const code, winrt::hresult_error::from_abi_t) noexcept;
```

### Parameters
`other`
Another **hresult_error** that initializes the **hresult_error** object.

`code`
An HRESULT code that initializes the **hresult_error** object.

`message`
An informative string to help developers to correct the reported error condition.

`object`
An error object that stores extra information about the error. The error object should be apartment-agile, in-proc, and marshal-by-value across processes. It should implement [ILanguageExceptionStackBackTrace](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionstackbacktrace) and [ILanguageExceptionTransform](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptiontransform) if necessary. See [RoOriginateLanguageException](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginatelanguageexception).

## hresult_error::code function
Retrieves the code for the error represented by the **hresult_error** object.

### Syntax
```cppwinrt
HRESULT code() const noexcept;
```

### Return value 
An HRESULT error code.

## hresult_error::from_abi static data member
An instance of type [hresult_error::from_abi_t](#hresult_errorfrom_abi_t-type), which can be passed to the constructor of **hresult_error** (or a derived type) to indicate that the constructor should try to retrieve restricted error info.

### Syntax
```cppwinrt
static constexpr winrt::hresult_error::from_abi_t from_abi{};
```

## hresult_error::from_abi_t type
The type of the [hresult_error::from_abi](#hresult_errorfrom_abi-static-data-member) static data member.

### Syntax
```cppwinrt
struct from_abi_t {};
```

## hresult_error::message function
Retrieves the message for the error represented by the **hresult_error** object.

### Syntax
```cppwinrt
winrt::hstring message() const noexcept;
```

### Return value
A [winrt::hstring](../hstring.md) containing the error messsage.

## hresult_error::operator= (assignment operator)
Assigns a value to the **hresult_error** object.

### Syntax
```cppwinrt
winrt::hresult_error& operator=(winrt::hresult_error&&);
winrt::hresult_error& operator=(winrt::hresult_error const& other) noexcept;
```

### Parameters
`other`
An **hresult_error** value to assign to the **hresult_error** object.

### Return value
A reference to the **hresult_error** object.

## hresult_error::to_abi function
Sets the restricted error information object for the current thread, and returns the code for the error represented by the **hresult_error** object.

### Syntax
```cppwinrt
HRESULT to_abi() const noexcept;
```

### Return value
An HRESULT error code.

## hresult_error::try_as function
Returns the requested interface, if it is supported. Returns `nullptr` if it is not. This function is useful if you want to query for an interface that you don't need to pass back to your caller. For example, you can retrieve an [IRestrictedErrorInfo](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-irestrictederrorinfo) to access the restricted error info for the error represented by the **hresult_error** object.

### Syntax
```cppwinrt
template <typename To> auto try_as() const noexcept;
```

### Template parameters
`typename To`
The type of the requested interface.

### Parameters
`to`
A reference to a value to receive the requested interface.

### Return value
A [winrt::com_ptr](../com-ptr.md) referencing the requested interface, or a strongly-typed smart pointer for the requested interface (either declared by C++/WinRT or by a third party), if the requested interface is supported, otherwise `nullptr`.

## See also 
* [winrt namespace](../winrt.md)
* [winrt::com_ptr struct template](../com-ptr.md)
* [ILanguageExceptionStackBackTrace interface](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionstackbacktrace)
* [ILanguageExceptionTransform interface](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptiontransform)
* [RoOriginateLanguageException function](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginatelanguageexception)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)
