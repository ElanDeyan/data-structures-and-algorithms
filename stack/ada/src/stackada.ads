pragma Ada_2022;
pragma Extensions_Allowed (On);

with Ada.Containers.Vectors;
generic
   type Element_Type is private;
   type Index_Type is range <>;

package Stackada is
   type Unbounded_Stack is tagged private;

   type Elements_Array is array (Index_Type range <>) of Element_Type;

   type Maybe (Has_Element : Boolean := False) is record
      case Has_Element is
         when True =>
            Value : Element_Type;
         when False =>
            null;
      end case;
   end record;

   subtype None is Maybe (Has_Element => False);
   subtype Just is Maybe (Has_Element => True);

   procedure Push (Stack : in out Unbounded_Stack; Element : Element_Type) with
      Post => (Stack.Length = Stack'Old.Length + 1)
      and then (Stack.Contains (Element));

   procedure Push_All
     (Stack : in out Unbounded_Stack; Elements : Elements_Array) with
      Post => Stack.Length = Stack'Old.Length + Elements'Length;

   function Pop (Stack : in out Unbounded_Stack) return Element_Type with
      Pre  => Stack.Is_Not_Empty,
      Post => Stack.Length = Stack'Old.Length - 1;

   function Try_Pop (Stack : in out Unbounded_Stack) return Maybe;

   procedure Pop
     (Stack : in out Unbounded_Stack; Output : out Element_Type) with
      Pre  => Stack.Is_Not_Empty,
      Post => Stack.Length = Stack'Old.Length - 1;

   procedure Try_Pop (Stack : in out Unbounded_Stack; Output : out Maybe);

   function Peek (Stack : in out Unbounded_Stack) return Element_Type with
      Pre => Stack.Is_Not_Empty;

   function Try_Peek (Stack : in out Unbounded_Stack) return Maybe;

   procedure Peek
     (Stack : in out Unbounded_Stack; Output : out Element_Type) with
      Pre => Stack.Is_Not_Empty;

   procedure Try_Peek (Stack : in out Unbounded_Stack; Output : out Maybe);

   function Is_Empty (Stack : Unbounded_Stack) return Boolean;

   function Is_Not_Empty (Stack : Unbounded_Stack) return Boolean;

   function Length (Stack : Unbounded_Stack) return Natural;

   function Contains
     (Stack : Unbounded_Stack; Element : Element_Type) return Boolean;

   Empty_Stack_State : exception;

private
   package Vectors is new Ada.Containers.Vectors
     (Index_Type => Index_Type, Element_Type => Element_Type);

   use Vectors;
   type Unbounded_Stack is tagged record
      Internal_Container : Vectors.Vector;
   end record;
end Stackada;
