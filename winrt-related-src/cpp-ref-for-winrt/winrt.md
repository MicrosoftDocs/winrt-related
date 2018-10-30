---
author: stevewhims
description: API reference content for the winrt namespace from C++/WinRT.
title: winrt namespace (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/10/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt namespace (C++/WinRT)

The **winrt** namespace provides custom data types belonging to [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt)&mdash;the standard, modern C++17 language projection for Windows Runtime (WinRT) APIs. These custom types provide appropriate conversions to and from standard types so that, much of the time, you can continue to use the standard C++ language features that you're accustomed to using, and the source code that you already have.

Also provided in the **winrt** namespace are functions (for creating runtime class instances, boxing and unboxing, etc.), smart pointers, and other facilities.

## Types in the winrt namespace
| Type | Description |
| - | - |
| [agile_ref struct template](agile-ref.md) | A type representing an agile reference to a C++/WinRT object or interface. |
| [apartment_context struct](apartment-context.md) | Captures the thread context within a coroutine so that it can be restored later. |
| [array_view struct template](array-view.md) | A view, or span, of a contiguous series of values. |
| [auto_revoke_t marker struct](auto-revoke-t.md) | A marker type used to request an event revoker when registering a delegate to handle an event. |
| [clock struct](clock.md) | A type containing static helper functions for converting a [Windows::Foundation::DateTime](/uwp/api/windows.foundation.datetime) (that is, a [std::chrono::time_point](/cpp/standard-library/time-point-class)) to and from **winrt::file_time**, and to and from [time_t](/cpp/c-runtime-library/reference/time-time32-time64). |
| [com_array struct template](com-array.md) | A view, or span, of a contiguous series of values for passing to and from Windows Runtime APIs. |
| [com_ptr struct template](com-ptr.md) | A reference-counted COM smart pointer template. |
| [delegate struct template](delegate.md) | A type that you can use to declare a custom delegate type for your own events. |
| [event struct template](event.md) | A type that you can use to declare and implement an event of a specified delegate type. |
| [event_revoker struct template](event-revoker.md) | When you register a delegate, you can request an event revoker, which you can use to automatically or manually revoke your delegate. |
| [event_token struct](event-token.md) | A token returned when registering an event-handling delegate with an event; can be used to revoke the registration of the same delegate. |
| [file_handle struct](file-handle.md) | Represents a Windows file handle object. |
| [fire_and_forget struct](fire-and-forget.md) | Use this return type to make your coroutine a fire-and-forget one. |
| [handle struct](handle.md) | Represents a Windows handle object. |
| [handle_type struct template](handle-type.md) | The template for the [**winrt::handle**](handle.md) and [**winrt::file_handle**](file-handle.md) structs. |
| [hstring struct](hstring.md) | A sequential collection of UTF-16 Unicode characters representing a text string. |
| [hresult_access_denied struct](error-handling/hresult-access-denied.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_ACCESSDENIED HRESULT error code. |
| [hresult_canceled struct](error-handling/hresult-canceled.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an ERROR_CANCELLED HRESULT error code. |
| [hresult_changed_state struct](error-handling/hresult-changed-state.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_CHANGED_STATE HRESULT error code. |
| [hresult_class_not_available struct](error-handling/hresult-class-not-available.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an CLASS_E_CLASSNOTAVAILABLE HRESULT error code. |
| [hresult_error struct](error-handling/hresult-error.md) | A type representing an HRESULT error code. |
| [hresult_illegal_delegate_assignment struct](error-handling/hresult-illegal-delegate-assignment.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_ILLEGAL_DELEGATE_ASSIGNMENT HRESULT error code. |
| [hresult_illegal_method_call struct](error-handling/hresult-illegal-method-call.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_ILLEGAL_METHOD_CALL HRESULT error code. |
| [hresult_illegal_state_change struct](error-handling/hresult-illegal-state-change.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_ILLEGAL_STATE_CHANGE HRESULT error code. |
| [hresult_invalid_argument struct](error-handling/hresult-invalid-argument.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_INVALIDARG HRESULT error code. |
| [hresult_no_interface struct](error-handling/hresult-no-interface.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_NOINTERFACE HRESULT error code. |
| [hresult_not_implemented struct](error-handling/hresult-not-implemented.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_NOTIMPL HRESULT error code. |
| [hresult_out_of_bounds struct](error-handling/hresult-out-of-bounds.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an E_BOUNDS HRESULT error code. |
| [hresult_wrong_thread struct](error-handling/hresult-wrong-thread.md) | A type derived from [winrt::hresult_error](error-handling/hresult-error.md), representing an RPC_E_WRONG_THREAD HRESULT error code. |
| [implements struct template](implements.md) | A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type. |
| [map_base struct template](map-base.md) | A base class, for you to derive from, that represents a non-observable associative collection. |
| [map_view_base struct template](map-view-base.md) | A base class, for you to derive from, that represents a view of a contiguous sequence of elements in an associative collection. |
| [no_weak_ref marker struct](no-weak-ref.md) | A marker type used to opt out of weak reference support. |
| [non_agile marker struct](non-agile.md) | A marker type used to indicate that your type is not agile, and consequently does not implement the [IAgileObject interface](https://msdn.microsoft.com/library/windows/desktop/hh802476). |
| [observable_map_base struct template](observable-map-base.md) | A base class, for you to derive from, that represents an observable associative collection. |
| [observable_vector_base struct template](observable-vector-base.md) | A base class, for you to derive from, that represents an observable vector. |
| [resume_foreground struct](resume-foreground.md) | A struct&mdash;for use within a coroutine&mdash;that you can `co_await` to switch execution to a specific foreground thread. |
| [vector_base struct template](vector-base.md) | A base class, for you to derive from, that represents a non-observable general-purpose collection known as a vector. |
| [vector_view_base struct template](vector-view-base.md) | A base class from which you can derive to implement your own custom view, or span, of a contiguous sequence of elements in a general-purpose collection. |
| [weak_ref struct template](weak-ref.md) | A type representing a weak reference to a C++/WinRT object or interface. |
| [Windows::Foundation::IUnknown struct](windows-foundation-iunknown.md) | Every C++/WinRT runtime class (whether a Windows or a third party runtime class) derives from winrt::Windows::Foundation::IUnknown. |

## Functions in the winrt namespace
| Function | Description |
| - | - |
| [attach_abi function](attach-abi.md) | A helper function that attaches a C++/WinRT object to a handle, or to a raw pointer that owns a reference to its target. |
| [box_value function template](box-value.md) | A function template that wraps (or *boxes*) a scalar value inside a reference class object so that it can be passed to a function that expects **IInspectable**. |
| [check_bool function template](error-handling/check-bool.md) | A helper function that checks whether a value is false and, if so, retrieves the calling thread's last-error code value, and throws an exception using a C++/WinRT object that represents that error code. |
| [check_hresult function](error-handling/check-hresult.md) | A helper function that checks whether an HRESULT code represents an error and, if so, throws an exception using a C++/WinRT object that represents the error code. |
| [check_nt function template](error-handling/check-nt.md) | A helper function that checks whether a code represents an error and, if so, maps the NT status value of the error code to an HRESULT value and throws an exception using a C++/WinRT object that represents the error code. |
| [check_pointer function template](error-handling/check-pointer.md) | A helper function that checks whether a pointer is null and, if so, retrieves the calling thread's last-error code value, and throws an exception using a C++/WinRT object that represents that error code. |
| [check_win32 function template](error-handling/check-win32.md) | A helper function that checks whether a code represents an error and, if so, maps the system error code of the value to an HRESULT value and throws an exception using a C++/WinRT object that represents the error code. |
| [copy_from_abi function](copy-from-abi.md) | A helper function that copies to a C++/WinRT object from a handle, or from a raw pointer. |
| [copy_to_abi function](copy-to-abi.md) | A helper function that copies to a handle, or to a pointer from a C++/WinRT object. |
| [detach_abi function](detach-abi.md) | A helper function that detaches a C++/WinRT object from its referenced handle, or from its referenced interface. |
| [from_abi function template](from-abi.md) | A helper function which, given an object of a projected type, retrieves a pointer to the implementation. |
| [get_abi function](get-abi.md) | A helper function that retrieves a pointer to a C++/WinRT object's underlying [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509). |
| [get_activation_factory function template](get-activation-factory.md) | A helper function that retrieves the activation factory for a specified Windows Runtime class type. |
| [get_cancellation_token function](get-cancellation-token.md) | In a coroutine, use the object returned by **winrt::get_cancellation_token** to poll for, or to respond to, cancellation. |
| [get_class_name function](get-class-name.md) | A helper function that retrieves a string containing the fully-qualified type name of a specified Windows Runtime class. |
| [get_interfaces function](get-interfaces.md) | A helper function that retrieves an array containing the identifiers of the interfaces that are implemented by a C++/WinRT object. |
| [get_progress_token function](get-progress-token.md) | In a coroutine, use the object returned by **winrt::get_progress_token** to report progress back to a progress handler. |
| [get_self function template](get-self.md) | A helper function which, given an object of a projected type, retrieves a pointer to the implementation. |
| [get_trust_level function](get-trust-level.md) | A helper function that retrieves the trust level of a C++/WinRT object. |
| [make function template](make.md) | A factory method that returns an instance of a projected type or interface when parameterized with the corresponding implementation type. |
| [make_agile function template](make-agile.md) | A helper function that returns an [agile_ref](agile-ref.md) object, representing an agile reference to a C++/WinRT object or interface. |
| [make_self function template](make-self.md) | A factory method that returns a [com_ptr](com-ptr.md) to an instance of the implementation type for a runtime class. |
| [make_weak function template](make-weak.md) | A helper function that returns a [weak_ref](weak-ref.md) object, representing a weak reference to a C++/WinRT object or interface. |
| [put_abi function](put-abi.md) | A helper function that retrieves the address of a C++/WinRT object's underlying IUnknown interface pointer so that it can be set to another value. |
| [resume_background function](resume-background.md) | A helper function that returns control to the caller, and resumes execution on a thread pool thread. |
| [single_threaded_map function template](single-threaded-map.md) | A function template that creates and returns an object of a type that implements a non-observable associative collection (map). The object is returned as an [**IMap**](/uwp/api/windows.foundation.collections.imap_k_v_). |
| [single_threaded_observable_map function template](single-threaded-observable-map.md) | A function template that creates and returns an object of a type that implements an observable associative collection (map). The object is returned as an [**IObservableMap**](/uwp/api/windows.foundation.collections.iobservablemap_k_v_). |
| [single_threaded_observable_vector function template](single-threaded-observable-vector.md) | A function template that creates and returns an object of a type that implements an observable collection. The object is returned as an [**IObservableVector**](/uwp/api/windows.foundation.collections.iobservablevector_t_). |
| [single_threaded_vector function template](single-threaded-vector.md) | A function template that creates and returns an object of a type that implements a general-purpose collection. The object is returned as an [**IVector**](/uwp/api/windows.foundation.collections.ivector_t_). |
| [swap function](swap.md) | A helper function that swaps the contents of two values. |
| [throw_hresult function](error-handling/throw-hresult.md) | A helper function that takes a HRESULT error code, and throws an exception using a C++/WinRT object that represents that error code. |
| [throw_last_error function](error-handling/throw-last-error.md) | A helper function that retrieves the calling thread's last-error code value, and throws an exception using a C++/WinRT object that represents that error code. |
| [to_hresult function](error-handling/to-hresult.md) | A helper function, for use in a catch block, that turns the last exception thrown into a HRESULT error code. |
| [to_hstring function](to-hstring.md) | A helper function that converts an input value to a **winrt::hstring** containing the value's string representation. |
| [to_string function](to-string.md) | A helper function that converts an input wide string to a **std::string** containing a UTF-8 narrow string. |
| [unbox_value function template](unbox-value.md) | A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object so that it can be processed in a function that expects **IInspectable**. |
| [unbox_value_or function template](unbox-value-or.md) | A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object, with a fallback value, so that it can be processed in a function that expects **IInspectable**. |
| [xaml_typename function template](xaml-typename.md) | A helper function that returns the type name of a Windows Runtime type, in the form of a [Windows::UI::Xaml::Interop::TypeName](/uwp/api/windows.ui.xaml.interop.typename) object. |

## Other functions
| Function | Description |
| - | - |
| [GetRuntimeClassName function](getruntimeclassname.md) | A member function (of a generated implementation type) that returns a string containing the fully-qualified type name of the Windows Runtime class being implemented. |

## See also 
[C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index)
