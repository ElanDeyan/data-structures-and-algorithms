with Ada.Containers.Vectors;

generic
   type E is private;
   type I is range <>;

package Queueada with
   SPARK_Mode
is

   type Unbounded_Queue is tagged private;

   type Elements_Array is array (I range <>) of E;

   type Maybe (Has_Element : Boolean := False) is record
      case Has_Element is
         when True =>
            Value : E;
         when others =>
            null;
      end case;
   end record;

   subtype None is Maybe (Has_Element => False);
   subtype Just is Maybe (Has_Element => True);

   Empty_Queue_State : exception;

   function Is_Empty (Queue : Unbounded_Queue) return Boolean with
      Pure_Function,
      Inline;

   function Is_Not_Empty (Queue : Unbounded_Queue) return Boolean with
      Pure_Function,
      Inline;

   function Contains (Queue : Unbounded_Queue; Element : E) return Boolean with
      Pure_Function,
      Inline;

   function Length (Queue : Unbounded_Queue) return Natural with
      Pure_Function,
      Inline;

   function Peek (Queue : Unbounded_Queue) return E with
      Pre => Queue.Length >= 0,
      Pure_Function,
      Inline;

   procedure Peek (Queue : Unbounded_Queue; Output : out E) with
      Pre     => Queue.Length >= 0,
      Depends => (Output => Queue),
      Global  => null;

   function Try_Peek (Queue : Unbounded_Queue) return Maybe with
      Pure_Function,
      Inline;

   procedure Try_Peek (Queue : Unbounded_Queue; Output : out Maybe) with
      Depends => (Output => Queue),
      Global  => null;

   procedure Enqueue (Queue : in out Unbounded_Queue; Element : E) with
      Post => Queue.Contains (Element)
      and then Queue.Length = Queue'Old.Length + 1;

   procedure Enqueue_All
     (Queue : in out Unbounded_Queue; Elements : Elements_Array) with
      Post =>
      (for all Index in Elements'Range => Queue.Contains (Elements (Index)))
      and then Queue.Length = Queue'Old.Length + Elements'Length;

   function Dequeue (Queue : in out Unbounded_Queue) return E with
      Pre  => Queue.Is_Not_Empty,
      Post => Queue.Length = Queue'Old.Length - 1;

   function Try_Dequeue (Queue : in out Unbounded_Queue) return Maybe;

   procedure Dequeue (Queue : in out Unbounded_Queue; Output : out E) with
      Pre  => Queue.Is_Not_Empty,
      Post => Queue.Length = Queue'Old.Length - 1;

   procedure Try_Dequeue (Queue : in out Unbounded_Queue; Output : out Maybe);

private

   package Vectors is new Ada.Containers.Vectors
     (Index_Type => I, Element_Type => E);

   use Vectors;

   type Unbounded_Queue is tagged record
      Internal_Container : Vectors.Vector;
   end record;

end Queueada;
