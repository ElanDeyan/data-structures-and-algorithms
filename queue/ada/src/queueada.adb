package body Queueada with
   SPARK_Mode
is
   function Is_Empty (Queue : Unbounded_Queue) return Boolean is
     (Queue.Internal_Container.Is_Empty);

   function Is_Not_Empty (Queue : Unbounded_Queue) return Boolean is
     (not Queue.Is_Empty);

   function Contains (Queue : Unbounded_Queue; Element : E) return Boolean is
     (Queue.Internal_Container.Contains (Element));

   function Length (Queue : Unbounded_Queue) return Natural is
     (Natural (Queue.Internal_Container.Length));

   function Peek (Queue : Unbounded_Queue) return E is
   begin
      if Queue.Is_Empty then
         raise Empty_Queue_State with "Empty queue";
      end if;

      return Queue.Internal_Container.First_Element;
   end Peek;

   procedure Peek (Queue : Unbounded_Queue; Output : out E) is
   begin
      if Queue.Is_Empty then
         raise Empty_Queue_State with "Empty queue";
      end if;

      Output := Queue.Internal_Container.First_Element;
   end Peek;

   function Try_Peek (Queue : Unbounded_Queue) return Maybe is
      Nothing : None;
      First   : Just;
   begin
      return Result : Maybe := Nothing do
         if Queue.Is_Not_Empty then
            Result       := First;
            Result.Value := Queue.Internal_Container.First_Element;
         end if;
      end return;
   end Try_Peek;

   procedure Try_Peek (Queue : Unbounded_Queue; Output : out Maybe) is
      Nothing : None;
      First   : Just;
   begin
      if Queue.Is_Not_Empty then
         Output       := First;
         Output.Value := Queue.Internal_Container.First_Element;
      else
         Output := Nothing;
      end if;
   end Try_Peek;

   procedure Enqueue (Queue : in out Unbounded_Queue; Element : E) is
   begin
      Queue.Internal_Container.Append (Element);
   end Enqueue;

   procedure Enqueue_All
     (Queue : in out Unbounded_Queue; Elements : Elements_Array)
   is
   begin
      for Element of Elements loop
         Queue.Enqueue (Element);
      end loop;
   end Enqueue_All;

   function Dequeue (Queue : in out Unbounded_Queue) return E is
   begin
      if Queue.Is_Empty then
         raise Empty_Queue_State with "Dequeue in an empty queue.";
      end if;

      return Result : constant E := Queue.Internal_Container.First_Element do
         Queue.Internal_Container.Delete_First (1);
      end return;
   end Dequeue;

   procedure Dequeue (Queue : in out Unbounded_Queue; Output : out E) is
   begin
      if Queue.Is_Empty then
         raise Empty_Queue_State with "Dequeue in an empty queue.";
      end if;

      Output := Queue.Internal_Container.First_Element;

      Queue.Internal_Container.Delete_First (1);
   end Dequeue;

   function Try_Dequeue (Queue : in out Unbounded_Queue) return Maybe is
      Nothing : None;
      First   : Just;
   begin
      return Result : Maybe := Nothing do
         if Queue.Is_Not_Empty then
            Result       := First;
            Result.Value := Queue.Internal_Container.First_Element;
            Queue.Internal_Container.Delete_First (1);
         end if;
      end return;
   end Try_Dequeue;

   procedure Try_Dequeue (Queue : in out Unbounded_Queue; Output : out Maybe)
   is
      Nothing : None;
      First   : Just;
   begin
      if Queue.Is_Not_Empty then
         Output       := First;
         Output.Value := Queue.Internal_Container.First_Element;
         Queue.Internal_Container.Delete_First (1);
      else
         Output := Nothing;
      end if;
   end Try_Dequeue;

end Queueada;
