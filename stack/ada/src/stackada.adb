package body Stackada is
   procedure Push (Stack : in out Unbounded_Stack; Element : Element_Type) is
   begin
      Stack.Internal_Container.Append (Element);
   end Push;

   procedure Push_All
     (Stack : in out Unbounded_Stack; Elements : Elements_Array)
   is
   begin
      for Element of Elements loop
         Stack.Push (Element);
      end loop;
   end Push_All;

   function Pop (Stack : in out Unbounded_Stack) return Element_Type is

      Last_Element : Element_Type;
   begin
      if Stack.Is_Empty then
         raise Empty_Stack_State with "Tried to pop in empty stack";
      end if;

      Last_Element := Stack.Internal_Container.Last_Element;

      Stack.Internal_Container.Delete_Last (1);

      return Last_Element;
   end Pop;

   function Try_Pop (Stack : in out Unbounded_Stack) return Maybe is
      Last         : Just;
      Nothing      : None;
      Last_Element : Element_Type;
   begin
      if Stack.Is_Empty then
         return Nothing;
      end if;

      Last_Element := Stack.Internal_Container.Last_Element;

      Last.Value := Last_Element;

      Stack.Internal_Container.Delete_Last (1);

      return Last;
   end Try_Pop;

   procedure Pop (Stack : in out Unbounded_Stack; Output : out Element_Type) is
   begin
      if Stack.Is_Empty then
         raise Empty_Stack_State with "Tried to pop in a empty stack";
      end if;

      Output := Stack.Internal_Container.Last_Element;

      Stack.Internal_Container.Delete_Last (1);
   end Pop;

   procedure Try_Pop (Stack : in out Unbounded_Stack; Output : out Maybe) is
      Last         : Just;
      Nothing      : None;
      Last_Element : Element_Type;
   begin
      if Stack.Is_Empty then
         Output := Nothing;
      end if;

      Last_Element := Stack.Internal_Container.Last_Element;

      Last.Value := Last_Element;

      Output := Last;
      Stack.Internal_Container.Delete_Last (1);
   end Try_Pop;

   function Peek (Stack : in out Unbounded_Stack) return Element_Type is
   begin
      if Stack.Is_Empty then
         raise Empty_Stack_State with "Stack is empty";
      end if;

      return Stack.Internal_Container.Last_Element;
   end Peek;

   function Try_Peek (Stack : in out Unbounded_Stack) return Maybe is
      Last         : Just;
      Nothing      : None;
      Last_Element : Element_Type;
   begin
      if Stack.Is_Empty then
         return Nothing;
      end if;

      Last_Element := Stack.Internal_Container.Last_Element;

      Last.Value := Last_Element;

      return Last;
   end Try_Peek;

   procedure Peek (Stack : in out Unbounded_Stack; Output : out Element_Type)
   is
   begin
      if Stack.Is_Empty then
         raise Empty_Stack_State with "Empty stack";
      end if;

      Output := Stack.Internal_Container.Last_Element;
   end Peek;

   procedure Try_Peek (Stack : in out Unbounded_Stack; Output : out Maybe) is
      Last    : Just;
      Nothing : None;
   begin
      if Stack.Is_Empty then
         Output := Nothing;
      end if;

      Last.Value := Stack.Internal_Container.Last_Element;

      Output := Last;
   end Try_Peek;

   function Is_Empty (Stack : Unbounded_Stack) return Boolean is
     (Stack.Internal_Container.Is_Empty);

   function Is_Not_Empty (Stack : Unbounded_Stack) return Boolean is
     (not Stack.Internal_Container.Is_Empty);

   function Length (Stack : Unbounded_Stack) return Natural is
     (Natural (Stack.Internal_Container.Length));

   function Contains
     (Stack : Unbounded_Stack; Element : Element_Type) return Boolean is
     (Stack.Internal_Container.Contains (Element));
end Stackada;
