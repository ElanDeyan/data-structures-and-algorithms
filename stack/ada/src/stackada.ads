pragma Ada_2022;
pragma Extensions_Allowed (On);

with Ada.Containers.Vectors;
generic
    -- Type of the content
    type Element_Type is private;
    -- Type of the index of internal vector
    type Index_Type is range <>;

package Stackada is
    type Unbounded_Stack is limited private;

    type Elements_Array is array(Index_Type) of Element_Type;

    procedure Push (Stack: in out Unbounded_Stack; Element: in Element_Type);

    procedure Push_All (Stack: in out Unbounded_Stack; Elements : in Elements_Array);

    function Pop (Stack: in out Unbounded_Stack) return Element_Type
        with Pre => Stack.Is_Not_Empty;
    
    procedure Pop (Stack: in out Unbounded_Stack; Output: out Element_Type)
        with Pre => Stack.Is_Not_Empty;

    function Peek (Stack: in out Unbounded_Stack) return Element_Type
        with Pre => Stack.Is_Not_Empty;
    
    procedure Peek (Stack: in out Unbounded_Stack; Output: out Element_Type)
        with Pre => Stack.Is_Not_Empty;

    function Is_Empty (Stack: in Unbounded_Stack) return Boolean;

    function Is_Not_Empty (Stack: in Unbounded_Stack) return Boolean;

    function Length (Stack: in Unbounded_Stack) return Natural;

    function Contains (Stack: in Unbounded_Stack; Element: in Element_Type) return Boolean;

    Empty_Stack_State: exception;

private
    package Vectors is new Ada.Containers.Vectors
      (Index_Type   => Index_Type,
       Element_Type => Element_Type
       );

       use Vectors;
    type Unbounded_Stack is record
        Internal_Container: Vectors.Vector;
    end record;
end Stackada;
